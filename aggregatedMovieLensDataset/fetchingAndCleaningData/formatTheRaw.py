import json

fin = open("movieInfo.dat", "r")
fout = open("movielens_10m", "w")

count = 1
for line in fin:
    jsonObj = json.loads(line)
    out = {}
    out["id"] = [count]
    for key in jsonObj:
        if key!="poster" and key!="imdb_url" and key!="plot_simple" and key!="runtime" and key!="release_date" and key!="also_known_as" and key!="episodes":
            if key=="filming_locations":
                out[key] = jsonObj[key].replace(" ", "").split(",")
            elif key=="rating" or key=="rated" or key=="title" or key=="rating_count" or key=="year" or key=="type" or key=="imdb_id":
                out[key] = [jsonObj[key]]
            else:
                out[key] = jsonObj[key]
    count += 1
    #print type(json.dumps(out))
    #raw_input()
    fout.write(json.dumps(out) + "\n")

fout.close()
fin.close()