 #-*- coding: utf-8 -*-
 import os
 from flask import Flask, request, jsonify
 import json

 app = Flask(__name__)

 default_buttons = ['���̽� ����', '�� ����', '��ǻ�� ����']

 quiz_dict = {'python_quiz_buttons' : ['Guido van Rossum', 'Mark Elliot Zuckerberg', 'Geoffrey Everest Hinton', 'Yann LeCun', 'Andrew Ng'],
'web_quiz_buttons': ["HTML", "XML", "XHTML", "MXML", "JSON"],
'computer_quiz_buttons' : ['�ִϾ�', "�����", "�����", "���Ϲ�","�ϸ���"]}

answer_list = [quiz_dict['python_quiz_buttons'][0], quiz_dict['web_quiz_buttons'][1]]

choice_list = list(quiz_dict.values())[0]
for i in list(quiz_dict.values())[1:]:
    choice_list =  choice_list+ i


@app.route('/keyboard')
def keyboard():
    return jsonify({
        'type' : 'buttons',
        'buttons' : default_buttons
       })



@app.route('/message', methods=["POST"])
def true_or_false():
    dataRecieve = request.get_json()
    user_input = dataRecieve["content"]
    if user_input == default_buttons[0]:
        response_data = {
        'message' : {
            "text":'���� �ι��� �� ���̽��� �����ڴ� �����Դϱ�?'
        },
        "keyboard" : {
            "buttons" : quiz_dict['python_quiz_buttons'],
            "type" : "buttons",
          }
        }

    elif user_input == default_buttons[1]:

        response_data = {
          'message' : {
              "text":'���� ������ ��ũ���� �ƴѰ��� �����Դϱ�?'
          },
          "keyboard" : {
              "type" : "buttons",
              "buttons" : quiz_dict['web_quiz_buttons']
          }
        }
    elif user_input == default_buttons[2]:

        response_data = {
        'message' : {
            "text":'���� ������ ������ ��ǻ�ʹ� �����Դϱ�?'
        },
        "keyboard" : {
              "type" : "buttons",
              "buttons" : quiz_dict['computer_quiz_buttons']
             }
        }

    elif user_input in choice_list :
         if user_input in answer_list:
             response_data = {
                 'message' : {
                  "text":'�����Դϴ�. �ٸ� ��� Ǯ��ðھ��?'
                 },
                 "keyboard" : {
                     "type" : "buttons",
                     "buttons" : default_buttons
                    }
                }
    else:
        response_data = {
            'message' : {
                "text":'Ʋ�Ƚ��ϴ�. �ٸ� ��� Ǯ��ðھ��?'},
            "keyboard" : {
               "type" : "buttons",
               "buttons" : default_buttons
            }
          }

   return jsonify(response_data)


 if __name__=="__main__":
     app.run(host="0.0.0.0", port=5000)