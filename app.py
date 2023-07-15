

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import statsmodels.api as sm

st.title('Find the Carnatic Parent of the child raga :musical_keyboard: :musical_score:')


main_df=pd.read_csv('allragas.csv')

main_df=main_df[1:14].drop(['H_NOTES','C_NOTES','C_NOTES.1','base'],axis=1).astype(float)

twelve_swara=pd.DataFrame({'swaras':["s","r","R","g","G","m","M","P","d","D","n","N","S"],
    'frequency':[220.0,233.0,246.96,261.64,277.2,293.68,311.12,329.64,349.24,370.0,392.0,415.32,440.0]})


whose_child = st.text_input('Enter the child raga name:  ', '')
# st.write('Raga_name :', whose_child)
if whose_child!="":
    
    st.header('Reference table for swara input')
    st.dataframe(pd.read_csv('swara_set.csv'))

    input_child_raga_swara = st.multiselect(
        'Pick the swaras of the raga',
        ['s', 'r', 'R', 'g','G','m','M','P','d','D','n','N'],
        ['s'])

    input_child_raga_swara.append('S')

    st.write('You selected: '+ str(whose_child), input_child_raga_swara)

    whose_child=whose_child+" (child_raga)"

    if st.button('Generate_Result'):

        def picker(x):
                if x[0] not in input_child_raga_swara:
                    return 0
                else:
                    return x[1]

        test_data=twelve_swara.copy()
        test_data['frequency']=test_data[['swaras','frequency']].apply(picker,axis=1)
        child_raga=test_data['frequency']

        child_raga_swara=".".join(input_child_raga_swara).lower().split(".")

        new_columns=[]
        a=set(child_raga.loc[child_raga != 0])
        for i in main_df.columns:        
            if(a.union(set(main_df[i]))==set(main_df[i])):
                new_columns.append(i)
        df=main_df[new_columns].reset_index().drop('index',axis=1)

        df[whose_child]=pd.Series(child_raga)

        df['12_swaras']=pd.Series('s.r.R.g.G.m.M.p.d.D.n.N.S'.split("."))
        df['7_swaras']=pd.Series('s.r.r.g.g.m.m.p.d.d.n.n.s'.split("."))
        dfs=df
        x=list(dfs.columns)
        dfs.columns=x

        ic=input_child_raga_swara.copy()

        swaras = 's.r.R.g.G.m.M.p.d.D.n.N.S'.split(".")
        flag = 0

        for i in dfs.columns[:-2]:
            ic = [x.lower() for x in input_child_raga_swara]
            
            for j in range(len(swaras)):
                if len(ic)!=0:
                    if dfs[i].iloc[j] != 0 and dfs['7_swaras'][j] == ic[0]:
                        ic.pop(0)
                        
                        if dfs[whose_child][j] != dfs[i].iloc[j]:
                            flag = 1
                    
            if flag == 1:
                dfs = dfs.drop(i, axis=1)
                flag = 0

        st.dataframe(dfs[dfs.columns[:-1]])




        dfss=dfs[dfs.columns[:-2]]

        data = dfss

        correlations = {}
        p_values = {}

        for column in dfss.columns:
            if column != whose_child:
                correlation = data[whose_child].corr(data[column])
                correlations[column] = correlation

                X = sm.add_constant(data[column])
                model = sm.OLS(data[whose_child], X)
                results = model.fit()
                p_values[column] = results.pvalues[1]

        correlation_table = pd.DataFrame({'Correlation': correlations, 'P-value': p_values})
        correlation_table=correlation_table.sort_values(by='Correlation',ascending=False)
        st.write(correlation_table)

        dfs_bar=dfss.corr().sort_values(by=whose_child, ascending=False)[whose_child][1:]
        
        st.subheader("Raga Correlation Comparison")

        fig = px.bar(dfs_bar.reset_index(), x='index', y=whose_child  , color="index", title="")
        
        # dfs

        st.plotly_chart(fig, use_container_width=True)

        st.subheader('Also you can verify if the prediction/correlation is correct by verifying in the below link:')
        url='https://en.wikipedia.org/wiki/List_of_Janya_ragas'
        st.write("%s" % url)
   
    
