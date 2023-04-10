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
        ("Innovation", "Green Innovation"),
        ("Innovation", "Social Innovation"),
        ("Innovation", "Journalism Innovation"),
        ("Innovation", "Entrepreneurship"),
        ("Entrepreneurship", "Startup Opportunities"),
        ("Entrepreneurship", "Social Entrepreneurship"),
        ("Entrepreneurship", "Intrapreneurship"),
        ("Entrepreneurship", "Political Boycott"),
        ("Marketing", "Digital Marketing"),
        ("Marketing", "Content Marketing"),
        ("Marketing", "Customer Relationship Management"),
        ("Marketing", "Big Data Marketing"),
        ("Marketing", "Authentic Communication"),
        ("Marketing", "Social Media"),
        ("Education", "Innovation in Education"),
        ("Education", "Higher Education"),
        ("Education", "Entrepreneurship Education"),
        ("Education", "Teamwork in Education"),
        ("Organizational Behavior", "Absorptive Capacity"),
        ("Organizational Behavior", "Organizational Agility"),
        ("Organizational Behavior", "Job Satisfaction"),
        ("Organizational Behavior", "Cultural Fit"),
        ("Sustainability", "Green Supply Chain"),
        ("Sustainability", "Environmental Sustainability"),
        ("Sustainability", "Corporate Social Responsibility"),
        ("Tourism", "Cultural Tourism"),
        ("Tourism", "Environmental Attitudes"),
        ("Tourism", "Hotel Sector"),
        ("Tourism", "Destination Loyalty"),
        ("Technology", "Wireless Communications"),
        ("Technology", "Virtual Reality"),
        ("Technology", "Big Data"),
        ("Technology", "Artificial Intelligence"),
        # Conexiones entre clústeres
        ("Innovation", "Sustainability"),
        ("Innovation", "Technology"),
        ("Entrepreneurship", "Education"),
        ("Entrepreneurship", "Sustainability"),
        ("Marketing", "Education"),
        ("Marketing", "Organizational Behavior"),
        ("Marketing", "Tourism"),
        ("Education", "Organizational Behavior"),
        ("Education", "Technology"),
        ("Organizational Behavior", "Sustainability"),
        ("Organizational Behavior", "Technology"),
        ("Sustainability", "Tourism"),
        ("Sustainability", "Technology"),
        ("Tourism", "Technology"),
        ]

    st.title("")

    fig = create_knowledge_graph(edges)
    st.plotly_chart(fig)
