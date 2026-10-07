import torch

def get_video_replacement_qwen3vl(item_idx: int):
    """
    Extracts grid dimensions and calculates the vision token sequence length 
    for a specific video item in Qwen3-VL based preprocessing.
    """
    # 1. Extract the specific video item from the multimodel keyword arguments
    out_item = out_mm_kwargs["video"][item_idx]
    grid_thw = out_item["video_grid_thw"].data
    
    # 2. Validate tensor format
    assert isinstance(grid_thw, torch.Tensor), "grid_thw must be a torch.Tensor"
    assert grid_thw.ndim == 1 and grid_thw.shape[0] == 3, "grid_thw must be a 1D tensor with shape [3] (T, H, W)"

    # 3. Extract Grid components: Time (frames), Height, and Width chunks
    t, h, w = grid_thw[0].item(), grid_thw[1].item(), grid_thw[2].item()
    
    # 4. Calculate total visual tokens
    # Qwen-VL architectures downsample spatial blocks (typically H * W) over temporal frames (T)
    total_tokens = t * h * w
    
    return {
        "total_tokens": total_tokens,
        "grid_thw": (t, h, w),
        "pixel_values": out_item.get("pixel_values", None)
    }
