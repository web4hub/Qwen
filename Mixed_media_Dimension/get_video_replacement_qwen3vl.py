import torch
from typing import Sequence
from vllm.sequence import PromptUpdateDetails  # Standard wrapper used within vLLM engines

def get_video_replacement_qwen3vl(item_idx: int):
    # 1. Extract the current video multi-modal object from your dictionary
    out_item = out_mm_kwargs["video"][item_idx]
    grid_thw = out_item["video_grid_thw"].data
    assert isinstance(grid_thw, torch.Tensor)
    
    # 2. Extract corresponding metadata and timestamps for this item
    video, metadata = mm_items["video"][item_idx]
    
    # Calculate base tokens per frame based on the spatial grid dimensions (H * W) // merge_factor
    # Typically, Qwen3-VL downsamples patch arrays via a spatial factor 
    t_frames, h_grid, w_grid = grid_thw[0].item(), grid_thw[1].item(), grid_thw[2].item()
    num_tokens_per_frame = (h_grid * w_grid) // merge_length 

    # 3. Pull frame tokens or explicit timestamp arrays if tracked by the pipeline
    # Qwen3-VL features sparse token processing which injects frame-specific time identifiers
    frames_idx_token = metadata.get("frames_idx_token", []) 
    
    placeholder = []
    
    # 4. Construct the placeholder structure iteratively per frame block
    if frames_idx_token:
        for frame_idx in frames_idx_token:
            # Inject temporal metadata tokens (<X.X seconds>)
            placeholder.extend(frame_idx) 
            # Wrap structural vision embeddings with boundary tokens
            placeholder.extend(
                [vision_start_token_id] + 
                [video_token_id] * num_tokens_per_frame + 
                [vision_end_token_id]
            )
    else:
        # Fallback if frame token dictionary is unpopulated
        for _ in range(t_frames):
            placeholder.extend(
                [vision_start_token_id] + 
                [video_token_id] * num_tokens_per_frame + 
                [vision_end_token_id]
            )
            
    # Return mapped token selections wrapped to line up with the main input ID stream
    return PromptUpdateDetails.select_token_id(placeholder, video_token_id)
