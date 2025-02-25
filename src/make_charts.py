import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def make_chart(df, color_dict, x_range=[250, 0], leg_title='', ):
    fig = go.Figure()

    y_center = 0
    y_tick_positions = []
    for i, aa in enumerate(sorted(df['comp_id'].unique())):  # line 10
        #y_center = i  # each amino acid on its own horizontal line  # line 11
        for j, atom in enumerate(df[df['comp_id'] == aa]['atom_id'].unique()):  # line 12
            stats = df[(df['comp_id'] == aa) & (df['atom_id'] == atom)].iloc[0]  # line 13
            lowerfield = stats['lower']  # line 14
            upperfield = stats['higher']  # line 15
            box_offset = 0.2  # vertical thickness of each box  # line 16
            # Shift each box vertically based on its index j
            y0 = y_center - box_offset + j * (box_offset * 2)  # line 17
            y1 = y0 + box_offset * 1.5  # line 18
            fig.add_shape(
                type="rect",                      # line 19
                x0=lowerfield,                    # line 20
                x1=upperfield,                    # line 21
                y0=y0,                            # line 22
                y1=y1,                            # line 23
                fillcolor=color_dict[atom],  # line 24
                opacity=0.8,                      # line 25
                line=dict(color=color_dict[atom])  # line 26
            )
            fig.add_trace(go.Scatter(
                x=[(lowerfield + upperfield) / 2],
                y=[(y0 + y1) / 2],
                mode='markers',
                marker=dict(size=40, color='rgba(0,0,0,0)'),  # invisible marker
                hoverinfo='text',
                text=f"Amino acid: {aa}<br>Atom: {atom}<br>{round(lowerfield, 1)}-{round(upperfield, 1)} ppm",
                showlegend=False
            ))
        y_tick_positions.append(y_center)
        y_center = y1 + 1
        
    fig.update_yaxes(
        #tickvals=list(range(20)),  # line 30
        tickvals=y_tick_positions,
        ticktext=list(sorted(df['comp_id'].unique()))                     # line 31
    )

    for nitr, color in color_dict.items():  # e.g., new Line 28
        fig.add_trace(go.Scatter(
            x=[None],
            y=[None],
            mode='markers',
            marker=dict(size=10, color=color),
            name=nitr,
            showlegend=True
        ))  # new Line 29

    fig.update_layout(
        legend=dict(
            x=1.05,   # new Line 30
            y=1,      # new Line 31
            title=leg_title,
            orientation="v"
        )
    )  # new Line 32


    fig.update_layout(
        template='plotly_white',
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis_range=x_range, 
        yaxis_range=[y_tick_positions[-1]+2, y_tick_positions[0]-0.7],
        width=700,
        height=1000,
        margin={'t': 0, 'b': 0, 'r': 0, 'l': 0}
                    )  # line 32

    return fig