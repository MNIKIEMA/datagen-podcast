from tqdm.auto import tqdm
import json
import argparse

with open("./data/episode.json", encoding="utf-8") as f:
    episode_info = json.load(f)

with open("./data/transcription.json", encoding="utf-8") as f:
    transcription = json.load(f)


def process(transcription, episode_info):

    new_data = []

    window = 8  # number of sentences to combine
    stride = 3  # number of sentences to 'stride' over, used to create overlap
    # print(episode_info[0].keys())
    for episode_id, data in tqdm(transcription.items()):
        data = data["chunks"]
        # Align episode info with the transcription
        episode_data = [ep_info for ep_info in episode_info if ep_info["name"].startswith("#"+episode_id[11:])][0]
        # print(episode_data["name"], episode_id)
        for i in range(0, len(data), stride):
            i_end = min(len(data)-1, i+window)
            
            text = " ".join([text['text'] for text in data[i:i_end]])
            if len(text) != 0:

                new_data.append({
                    'start':  data[i]['timestamp'][0],
                    'end': data[i_end]['timestamp'][1],
                    'title': episode_data["name"],
                    'text': text,
                    'id': episode_data["id"],
                    'url': episode_data["external_urls"]["spotify"],
                    'published': episode_data["release_date"]
                })
    return new_data



def parse_args():

    parser =argparse.ArgumentParser()
    parser.add_argument()
    args = parser.parse_args()
    
    return args


def main():
    data = process(transcription, episode_info)

    with open("./data/dataset.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=3)


if __name__=="__main__":
    main()