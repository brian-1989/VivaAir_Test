#!/usr/bin/python3
""" Help functions for calling APIs.

"""
import requests


def id_api(i, n):
    """ This function calls the new hacker API, in the
    Topstories endpoint, and filters the ID of the stories.
    Return: A list with the ID of the stories.

    """
    from rest_framework import status
    from rest_framework.response import Response

    id_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?'
    id_response = requests.get(id_url)
    if int(i) > len(id_response.json()) or int(n) > len(id_response.json()):
        error_text = 'The length of the parameters exceeds\
            the number of stories recorded.'
        return Response(error_text, status=status.HTTP_400_BAD_REQUEST)
    ids = [id_response.json()[index] for index in range(int(i), int(n))]
    return ids


def history_api(ids):
    """ This function calls the new hacker API, in the
    Item endpoint, and filters the ID of the stories.
    Return: A list of stories, each story is in
    dictionary format, with id and title fields.

    """
    my_list = []
    for id in ids:
        my_dict = {}
        hist_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?'.format(id)
        hist_response = requests.get(hist_url)
        my_dict['ID'] = hist_response.json()['id']
        my_dict['título'] = hist_response.json()['title']
        my_list.append(my_dict)
    return my_list


if __name__ == "__main__":
    id_api()
    history_api()
