* Patreon: https://www.patreon.com/sd_hassan

# civitai-image-scraper
Downloads bulk images from Civitai that have a reaction count for a specific emoji reaction greater than your variable
Filters images in the response to only those that include a Prompt, saves the prompt as a caption text file matching the image name.
Outputted results are almost suitable for training. LORA's are included in prompts so to do is a toggle to remove LORA's from the saved text file, for now you can remove them manually if using this for training


# How to modify
Line 10, `api_key = "xxxxxxx"` change to your API key from Civitai account settings.

Line 20, `if image['stats']['heartCount'] > 10`

You can change the reaction type from heartCount to any other supported in the API 
At the time of this script creation, the supported reaction types are:

        "cryCount"

        "laughCount"
        
        "likeCount"
        
        "dislikeCount"
        
        "heartCount"
        
        "commentCount"
        
https://github.com/civitai/civitai/wiki/REST-API-Reference#get-apiv1images

# How to run
`pip install -r requirements.txt`

Replace line 10 API key with your API key

`python civitai-image.py`



# example![brave_0a4zJ0eXOn](https://user-images.githubusercontent.com/119671806/231275932-66eff47f-1073-4ce5-a0e4-c90b5ff8a145.gif)


