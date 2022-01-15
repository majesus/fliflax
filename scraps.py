#----------------------------------------------------#
st.write('###### Anexo 3. % de cobertura')
st.write('A continuación, te mostramos el % de cobertura alcanzada como dato complementario.')
value = round(df['Ri'].iloc[0] * 100 / P)
options = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": value, "name": "Cobertura %"}],
            }
        ],
    }
from streamlit_echarts import st_echarts
st_echarts(options=options, width="100%", key=0)

# https://plotly.com/python/gauge-charts/
import plotly.graph_objects as go
value1 = round(df['Ri'].iloc[0] * 100 / P)
fig = go.Figure(go.Indicator(
  mode = "gauge+number",
  value = value1,
  domain = {'x': [0, 1], 'y': [0, 1]},
  title = {'text': "Cobertura %"},
  gauge = {'axis': {'range': [0, P]}}))

st.plotly_chart(fig)
#----------------------------------------------------#
