def knowledge_graph_app():

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
                            title="Grafo de conocimiento de nuestro departamento",
                            titlefont=dict(size=16),
                            showlegend=False,
                            hovermode="closest",
                            margin=dict(b=20, l=5, r=5, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )
        return fig

    edges = [
        ("Marketing", "Digital Marketing"),
        ("Marketing", "Content Marketing"),
        ("Marketing", "Customer Relationship Management"),
        ("Digital Marketing", "SEO"),
        ("Digital Marketing", "SEM"),
        ("Digital Marketing", "Social Media Marketing"),
        ("Content Marketing", "Influencer Marketing"),
        ("Content Marketing", "Video Marketing"),
        ("Customer Relationship Management", "Customer Retention"),
        ("Customer Relationship Management", "Customer Acquisition"),
        ("SEO", "On-page SEO"),
        ("SEO", "Off-page SEO"),
        ("SEM", "Google Ads"),
        ("SEM", "Facebook Ads"),
        ("Social Media Marketing", "Instagram Marketing"),
        ("Social Media Marketing", "LinkedIn Marketing"),
        ("Organizational Behavior", "Employee Motivation"),
        ("Organizational Behavior", "Teamwork"),
        ("Organizational Behavior", "Leadership"),
        ("Employee Motivation", "Job Satisfaction"),
        ("Employee Motivation", "Performance Management"),
        ("Teamwork", "Communication"),
        ("Teamwork", "Conflict Resolution"),
        ("Leadership", "Transformational Leadership"),
        ("Leadership", "Servant Leadership"),
        ("Entrepreneurship", "Startup Success"),
        ("Entrepreneurship", "Intrapreneurship"),
        ("Startup Success", "Innovation"),
        ("Startup Success", "Market Validation"),
        ("Intrapreneurship", "Employee Innovation"),
        # Añadiendo conexiones para interconectar áreas relevantes
        ("Marketing", "Entrepreneurship"),
        ("Organizational Behavior", "Entrepreneurship"),
        ("Digital Marketing", "Innovation"),
        ("Leadership", "Innovation"),
        ]

    st.title("")

    fig = create_knowledge_graph(edges)
    st.plotly_chart(fig)
