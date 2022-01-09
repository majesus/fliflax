# https://share.streamlit.io/andfanilo/streamlit-echarts-demo/master/app.py
from streamlit_echarts import st_echarts
import json        
with open("miserables.json", "r") as f:
    graph = json.loads(f.read())

for idx, node in enumerate(graph["nodes"]):
    graph["nodes"][idx]["label"] = {"show": node["symbolSize"] > 30}

option = {
    "title": {
        "text": "Les Miserables",
        "subtext": "Default layout",
        "top": "bottom",
        "left": "right",
    },
    "tooltip": {},
    "legend": [{"data": [a["name"] for a in graph["categories"]]}],
    "animationDuration": 1500,
    "animationEasingUpdate": "quinticInOut",
    "series": [
        {
            "name": "Les Miserables",
            "type": "graph",
            "layout": "none",
            "data": graph["nodes"],
            "links": graph["links"],
            "categories": graph["categories"],
            "roam": True,
            "label": {"position": "right", "formatter": "{b}"},
            "lineStyle": {"color": "source", "curveness": 0.3},
            "emphasis": {"focus": "adjacency", "lineStyle": {"width": 10}},
        }
    ],
}
st_echarts(option, height="500px")
