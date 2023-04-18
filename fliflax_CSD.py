import pandas as pd
import numpy as np

def CANEX(audience, insertion):
    return audience * (1 - np.exp(-insertion / audience))

def CSD(audiences, insertions, order, form):
    df = pd.DataFrame({"audience": audiences, "insertion": insertions})

    if order == "audience":
        df = df.sort_values(by="audience", ascending=False)
    elif order == "insertion":
        df = df.sort_values(by="insertion", ascending=False)
    elif order == "random":
        df = df.sample(frac=1)

    reach = 0
    exposure = []

    for i in range(len(df)):
        r = CANEX(df["audience"].iloc[i], df["insertion"].iloc[i])
        
        if form == "normal":
            reach = reach + r * (1 - reach)
        elif form == "inverse":
            reach = r + reach * (1 - r)
        elif form == "mixed":
            if i % 2 == 0:
                reach = reach + r * (1 - reach)
            else:
                reach = r + reach * (1 - r)
        
        exposure.append(reach)

    return reach, exposure

audiences = [125, 748, 250, 312]
insertions = [10, 2, 3, 4]
order = "audience"
form = "inverse"

reach, exposure = CSD(audiences, insertions, order, form)
st.write(f"El alcance de la campaña es {reach:.4f}")
st.write(f"La distribución de exposición de la campaña es {exposure}")
