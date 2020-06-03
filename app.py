# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:16:13 2020

@author: user
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash_table as dt
import dash_table


external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



# load dataset
#df = pd.read_csv("Day.csv")

markdown_text = '''
## **Prime - 4** (Supervised Machine Learning Training)
#### Schedule **19 to 23 May** (6 days Training Timing 5:00Pm - 7:00Pm)
#### Traning Fee : INR - only **500 /-INR**
######  Call or whatsapp. [+917851929944](/)
'''


list1 = ["Day0","Day1","Day2","Day3","Day4","Day5"]

df1 = pd.read_csv("Full_data_present_everyday.csv")
df2 = pd.read_csv("Not_present_any_day.csv")

list2 = ['Registered Name','Email','Gender','College Name','WhatsApp No.']



colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'color1': 'white',
    'color2': 'blue'
}

fig1=px.bar(df1, y ='Total',x = 'Zoom Name',
                text='Total',
                color='Total',
                hover_data=['Name','Gender','College Name','Email','WhatsApp No.','Day0','Day1','Day2','Day3','Day4','Day5'],
                height=450,
            )


list3 = ['Name_Reg','Email','Gender_Reg','College Name_Reg','WhatsApp No._Reg']

list4 = ['Name','Gender','College Name','Email','WhatsApp No.','Day0','Day1','Day2','Day3','Day4','Day5']
app.layout = html.Div( children=[
        
    html.H1(
        children='Forsk Coding School',
        style={
            'textAlign': 'center',
            'color': colors['color1'],
            'backgroundColor': colors['color2'],
            'borderRadius': '5px',
            'margin': '20px',
            'padding': '10px',
            'borderStyle': 'dashed',
            'margin-bottom':'0px',
            'font-size': '40px',
            'margin-top':'10px'
            
        }
    ),
    html.H3(
        children='-- Student Attendence Analysis --',
        style={
            'textAlign': 'center',
            'color': colors['color1'],
            'backgroundColor': colors['color2'],
            'borderRadius': '5px',
            'margin': 'auto',
            'margin-right':'20px',
            'margin-left':'20px',
            'font-size': '18px',
            'padding': '10px',
        }
    ),
    
    
    #Markdown (details of Prime)
    html.Div([dcc.Markdown(children=markdown_text)],
              style={
            'textAlign': 'center',
        }
    ),
    
    #dropdown (Days)
    html.Div([dcc.Dropdown(id='dd',
        options=[{'label': c , 'value': c} for c in list1],
        value='Day0')],
    style={
            'width':'40%',
            'padding':40
        }
    ),
    





    #Present Registered student
    html.H3(
        children='Registered & Present Student',
        style={
            'textAlign': 'center',
            'color': colors['color2'],
            'margin': 'auto',
            'font-size': '25px',
            'margin-bottom':'0px',
            'font': '20px Arial, sans-serif',
            
        }
    ),
    #graph1
    dcc.Graph(id = 'graph'),
    
    
    
    
    
    
    
    #Absent Students
    html.H3(
        children='Absent Students Table',
        style={
            'textAlign': 'center',
            'color': colors['color2'],
            'margin': 'auto',
            'font-size': '25px',
            'margin-bottom':'0px',
            'margin-top':'70px',
            'font': '20px Arial, sans-serif',
        }
    ),
    
    
    
    #Table
    html.Div(
            [
                    
                dash_table.DataTable(
                id='datatable-paging',
                columns=[
                    {"name": i, "id": i} for i in list2],
                     style_cell={'textAlign': 'left'}, 
               style_data={ 'border': '1px solid blue' ,
                           'margin-left':'20px',
                           'margin-right':'20px'},
                style_header={
                  'backgroundColor': 'rgb(230, 230, 230)',
                  'fontWeight': 'bold'
            },
              
#                        style={
#            'textAlign': 'center',
#            'color': colors['color2'],
#            'margin': 'auto',
#             }
                ),
                
                
            ], className = 'row'
        ),
    
    
    
    
    
    #Not Registered student
    html.H3(
        children='UnRegistered But Present',
        style={
            'textAlign': 'center',
            'color': colors['color2'],
            'margin': 'auto',
            'font-size': '25px',
            'margin-bottom':'0px',
            'margin-top':'70px',
            'font': '20px Arial, sans-serif',
        }
    ),
    
    #graph3
    dcc.Graph(id = 'graph3'),
    
    
    
    #Not present any day student
    html.H3(
        children='Full present students',
        style={
            'textAlign': 'center',
            'color': colors['color2'],
            'margin': 'auto',
            'font-size': '25px',
            'margin-bottom':'0px',
            'margin-top':'70px',
            'font': '20px Arial, sans-serif',
        }
    ),
    
    
     #graph4           
    dcc.Graph(figure=fig1),
        
        
        #Full data present
        html.H3(
            children='Not present any day student',
            style={
                'textAlign': 'center',
                'color': colors['color2'],
                'margin': 'auto',
                'font-size': '25px',
                'margin-bottom':'0px',
                'margin-top':'70px',
                'font': '20px Arial, sans-serif',
            }
        ),
        
         html.Div(
            [
                    
                dash_table.DataTable(
                data=df2.to_dict('records'),
                columns=[
                    {"name": i, "id": i} for i in list3],  
                     style_cell={'textAlign': 'left'}, 
               style_data={ 'border': '1px solid blue' ,
                           'margin-left':'20px',
                           'margin-right':'20px'},
                style_header={
                  'backgroundColor': 'rgb(230, 230, 230)',
                  'fontWeight': 'bold'
            },
              
#                        style={
#            'textAlign': 'center',
#            'color': colors['color2'],
#            'margin': 'auto',
#             }
                ),
                
                
            ], className = 'row'
        ),
           

        #search data             
        html.Div([
        dcc.Store(id = 'memory'),
        html.H3('Details of Particular Student:'),
        html.Div(
            [
                html.Div(
                    [
                        html.P('Search by:'),
                        dcc.Dropdown(
                                id = 'filter_x',
                                options=[
                                    {'label': 'No filter', 'value': 0},
                                    {'label': 'Name', 'value': 1},
                                    {'label': 'Email id', 'value': 2},
                                    {'label': 'Mobile No.', 'value': 3}
                                ],
                                value='0'
                        ),
                    ],
                    className='three columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Search From Here: '),
                        dcc.Input(
                                  id = 'filter_y',
                                  placeholder='Enter a value...',
                                  value=''
                              )  ,
                    ],
                    className='three columns',
                    style={'margin-top': '10','padding-left': '70px'}
                ),
                html.Div(
                    [
                        html.Button(children='Search Data', id='button_chart',n_clicks=0)
                    ],
                    className='one columns',
                    style={'padding-top': '30px'}
                )             
            ],
            className='row'
        ),
         html.Div(
            [
                    
                dash_table.DataTable(
                id='table',
                columns=[
                    {"name": i, "id": i} for i in list4],
                     style_cell={'textAlign': 'left'}, 
               style_data={ 'border': '1px solid blue' ,
                           'margin-left':'20px',
                           'margin-right':'20px'},
                style_header={
                  'backgroundColor': 'rgb(230, 230, 230)',
                  'fontWeight': 'bold',
                  
                  
            },
              
#                        style={
#            'textAlign': 'center',
#            'color': colors['color2'],
#            'margin': 'auto',
#             }
                ),
                
                
            ], className = 'row'
        ),
#        html.Div(
#            [
#                    
#                html.Div(id = 'table-box'),
#                html.Div(dt.DataTable(id = 'table', data=[{}]), style={'display': 'none'}),
#                
#                
#                
#            ], className = 'row'
#        ),
    ], className = 'row',  style = {'margin-top': 50, 'border':
                                    '1px solid #C6CCD5', 'padding': 15,
                                    'border-radius': '5px'})
   
#        id='Graph1',
#        figure={
#            'data': [
#                {'x': [1,2,3,4,5,6,7,8,9], 'y': [4, 1, 2,3,6,9,5,4,8], 'type': 'bar', 'name': 'SF'},
#                #{'x': [1,2,3,4,5,6,7,8,9], 'y': [2, 4, 5,6,8,3,1,9,6], 'type': 'bar', 'name': u'Montréal'},
#            ],
#            'layout': {
#                'plot_bgcolor': colors['color1'],
#                'paper_bgcolor': colors['background'],
#                'font': {
#                    'color': colors['text']
#                }
#            }
#        }
#    )
])
    
    


@app.callback(dash.dependencies.Output('graph','figure'),[dash.dependencies.Input('dd','value')])

def update_fig(value):
    try:
    
        dff = pd.read_csv("{}.csv".format(value))
        a = dff[(dff["Email"].isnull())].index[0]
        dff = dff.iloc[:a,]
        figure = px.bar(dff, y ='Time',x = 'Zoom Name',
                        text='Time',
                        color='Time',
                        hover_data=['Registered Name','Gender','College Name','Email'],
                        height=650,
                        )
        figure.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figure.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        
#        figure = {
#            'data':[
#            {'x': dff['Zoom Name'], 'y': dff['Time'], 'type': 'bar', 'name': 'SF'}
#            ],
#        'layout':{
#                'title' : 'Every student spend Time on Zoom',
#                'margin':{'t':0,'b':180},
#                'plot_bgcolor': colors['background'],
#                'paper_bgcolor': colors['background'],
#                'font': {
#                        'color': colors['text']
#                    }
#                
#            }
#        }
    except:
        return html.Div(['There was an error processing this file.'])
        
    return figure






@app.callback(dash.dependencies.Output('datatable-paging','data'),[dash.dependencies.Input('dd','value')])

def update_fig(value):
    try:
        dff = pd.read_csv("{}.csv".format(value))
        a = dff[(dff["Email"].isnull())].index[0]
        b = dff[(dff["Email"].isnull())].index[1]
        dff = dff.iloc[a+2:b,]
        data=dff.to_dict('records')
        return data
              

    except:
        return html.Div(['There was an error processing this file.'])
        
   








@app.callback(dash.dependencies.Output('graph3','figure'),[dash.dependencies.Input('dd','value')])

def update_fig(value):
    try:
        dff = pd.read_csv("{}.csv".format(value))
        b = dff[(dff["Email"].isnull())].index[1]
        dff = dff.iloc[b+2:,]
        figure = px.bar(dff, y ='Time',x = 'Zoom Name',
                        text='Time',
                        color='Time',
                        hover_data=['Email'],
                        height=500)
        figure.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figure.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
              

    except:
        return html.Div(['There was an error processing this file.'])
        
    return figure
    
#import plotly.express as px
#
#df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
#fig = px.bar(df, y='pop', x='country', text='pop')
#fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
#fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
#fig.show()
#             
    

@app.callback(dash.dependencies.Output('filter_y','type'),[dash.dependencies.Input('filter_x','value')])

def drop_value(value):
    if value == 1:
        type = "text"
        return type
    elif value == 2:
        type = "email"
        return type
    elif value == 3:
        type = "number"
        return type


@app.callback(
dash.dependencies.Output('table', 'data'),
[dash.dependencies.Input('button_chart', 'n_clicks')],
[dash.dependencies.State('filter_y', 'value')]
)

def update_figure(n_clicks, filename):
    df5 = pd.read_csv("Full_data_present_everyday.csv")
    if filename in df5["Name"].tolist():
        data=df5.to_dict('records')
        return data





if __name__ == '__main__':
    app.run_server()
    
    