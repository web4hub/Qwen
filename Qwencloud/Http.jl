using HTTP
using JSON

response = HTTP.post(
    "/v0/organizations/cloud-marketplace",
    [
        "Content-Type" => "application/json",
        "Authorization" => "Bearer YOUR_SECRET_TOKEN"
    ],
    JSON.json(Dict(
        "name" => "",
        "kind" => "",
        "size" => "",
        "buyer_id" => ""
    ))
)

println(String(response.body))
