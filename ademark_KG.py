import streamlit as st
import networkx as nx
import plotly.graph_objects as go

def create_knowledge_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines")

    node_x = [pos[node][0] for node in G.nodes()]
    node_y = [pos[node][1] for node in G.nodes()]

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode="markers",
        hoverinfo="text",
        marker=dict(
            showscale=True,
            colorscale="YlGnBu",
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title="Node Connections",
                xanchor="left",
                titleside="right"),
            line_width=2))
    
    offset = -0.05
    node_label_x = [pos[node][0] + offset for node in G.nodes()]
    node_label_y = [pos[node][1] + offset for node in G.nodes()]

    node_label_trace = go.Scatter(
        x=node_label_x, y=node_label_y,
        mode="text",
        hoverinfo="none",
        text=[node for node in G.nodes()],
        textposition="bottom center",
        textfont=dict(size=12, color="#000"))

    node_adjacencies = []
    node_text = []
    for node, adjacencies in G.adjacency():
        node_adjacencies.append(len(adjacencies))
        node_text.append(f"{node} - # of connections: {len(adjacencies)}")

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace, node_label_trace],
                    layout=go.Layout(
                        title="Knowledge Graph",
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode="closest",
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    return fig

edges = [
    ("Prioridades", "Valor al cliente"),
    ("Prioridades", "Martech y publicidad"),
    ("Prioridades", "Capturar información"),
    ("Prioridades", "Promoción omnicanal"),
    ("Prioridades", "Agilidad marketing"),
    ("Prioridades", "Innovación y desarrollo"),
    ("Prioridades", "Inclusión y diversidad"),

    ("Valor al cliente", "Viaje omnicanal"),
    ("Valor al cliente", "Tendencias macro"),

    ("Martech y publicidad", "Valor de marca"),
    ("Martech y publicidad", "Mensaje comunicación"),
    ("Martech y publicidad", "Estrategia de medios"),
    ("Martech y publicidad", "Interfaz cliente-tecnología"),

    ("Capturar información", "Visión cliente"),
    ("Capturar información", "KPI o métricas"),
    ("Capturar información", "Causalidad"),
    ("Capturar información", "Metodologías medición"),

    ("Promoción omnicanal", "Experiencia marca"),
    ("Promoción omnicanal", "Promoción marca"),
    ("Promoción omnicanal", "Distribución y demanda"),

    ("Agilidad marketing", "Capacidades y responsabilidades"),
    ("Agilidad marketing", "Entorno externo"),
    ("Agilidad marketing", "Cultura aprendizaje"),

    ("Innovación y desarrollo", "Ideas innovadoras"),
    ("Innovación y desarrollo", "Diseño productos"),
    ("Innovación y desarrollo", "Lanzamiento productos"),
    ("Innovación y desarrollo", "Medir éxito"),

    ("Inclusión y diversidad", "Problemas sociales y éticos"),
    ("Inclusión y diversidad", "Inclusión en estrategias"),
    ("Inclusión y diversidad", "Medir impacto"),
]


st.title("Marketing Knowledge Graph")

fig = create_knowledge_graph(edges)
st.plotly_chart(fig)

