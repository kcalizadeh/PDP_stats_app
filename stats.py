import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import numpy as np
# import os
# import boto3
import pickle
import plotly.express as px

from stats_functions import *



external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



# s3 = boto3.resource(
#     service_name='s3',
#     region_name='us-west-1',
#     aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
#     aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
# )



app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div([
                      dcc.Dropdown(id="stats-selection_1", 
                                  options=get_dropdown_list_stats(),
                                  style={'width': '90%'},
                                  placeholder='Start typing to search...'),  
                      dcc.Checklist(id='stats-options_1',
                                  options=get_checkbox_list(),
                                  value=['AWL', 'ASL', 'NUW',
                                        'FREQ', 'BGRAM', 'TXTS'],
                                  labelStyle={'display': 'inline-block', 
                                              'border-spacing': '2px'}),  
                      html.Div(id="stats-output-1", children=[])
                      ])),
                dbc.Col(html.Div([
                      dcc.Dropdown(id="stats-selection_2", 
                                  options=get_dropdown_list_stats(),
                                  style={'width': '90%'},
                                  placeholder='Start typing to search...'),  
                      dcc.Checklist(id='stats-options_2',
                                  options=get_checkbox_list(),
                                  value=['AWL', 'ASL', 'NUW',
                                        'FREQ', 'BGRAM', 'TXTS'],
                                  labelStyle={'display': 'inline-block'}),  
                      html.Div(id="stats-output-2", children=[])
                      ]))
            ]
        ),
    ]
)



@app.callback(Output(component_id="stats-output-1", component_property="children"),
              [Input(component_id="stats-selection_1", component_property="value"),
              Input(component_id='stats-options_1', component_property="value")])
def generate_stats_1(selection_value, checkbox_values):#, df=df, classifier_dict=classifier_dict):
  output_list = [html.Br()]
  if selection_value:
    with open(f'stats_pickles/{selection_value}_stats.pkl', 'rb') as st_dict:
      source_dict = pickle.load(st_dict)
  if 'TXTS' in checkbox_values and selection_value:
    title_list = source_dict['title_list']
    output_statement = f'**Titles in the Corpus:** {title_list}.'
    output_list.append(dcc.Markdown(output_statement))
  if 'ASL' in checkbox_values and selection_value:
    average_sentence_length = source_dict['mean_sent_length']
    output_statement = f'**Average Sentence Length:** {average_sentence_length} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    average_word_length = source_dict['mean_word_length']
    output_statement = f'**Average Word Length:** {average_word_length} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    num_unique, total_num = source_dict['num_unique']
    output_statement = f'**{num_unique}** unique words out of **{total_num}** total words.'
    output_list.append(dcc.Markdown(output_statement))
  if 'FREQ' in checkbox_values and selection_value:
    output_list.append(dcc.Graph(figure=source_dict['word_freq_chart']))
  if 'BGRAM' in checkbox_values and selection_value:
    output_list.append(dcc.Graph(figure=source_dict['ngram_chart']))
  return output_list



@app.callback(Output(component_id="stats-output-2", component_property="children"),
              [Input(component_id="stats-selection_2", component_property="value"),
              Input(component_id='stats-options_2', component_property="value")])
def generate_stats_2(selection_value, checkbox_values):#, df=df, classifier_dict=classifier_dict):
  output_list = [html.Br()]
  if selection_value:
    with open(f'stats_pickles/{selection_value}_stats.pkl', 'rb') as st_dict:
      source_dict = pickle.load(st_dict)
  if 'TXTS' in checkbox_values and selection_value:
    title_list = source_dict['title_list']
    output_statement = f'**Titles in the Corpus:** {title_list}.'
    output_list.append(dcc.Markdown(output_statement))
  if 'ASL' in checkbox_values and selection_value:
    average_sentence_length = source_dict['mean_sent_length']
    output_statement = f'**Average Sentence Length:** {average_sentence_length} words'
    output_list.append(dcc.Markdown(output_statement))
  if 'AWL' in checkbox_values and selection_value:
    average_word_length = source_dict['mean_word_length']
    output_statement = f'**Average Word Length:** {average_word_length} characters'
    output_list.append(dcc.Markdown(output_statement))
  if 'NUW' in checkbox_values and selection_value:
    num_unique, total_num = source_dict['num_unique']
    output_statement = f'**{num_unique}** unique words out of **{total_num}** total words.'
    output_list.append(dcc.Markdown(output_statement))
  if 'FREQ' in checkbox_values and selection_value:
    output_list.append(dcc.Graph(figure=source_dict['word_freq_chart']))
  if 'BGRAM' in checkbox_values and selection_value:
    output_list.append(dcc.Graph(figure=source_dict['ngram_chart']))
  return output_list

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)