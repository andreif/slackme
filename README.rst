slackme
=============

A tiny utility to send Slack messages using Incoming WebHook.

Installing

.. code:: sh

    $ pip install slackme

Help

.. code:: sh

    $ slackme -h
    usage: slackme [-h] [-v] [-n NAME] [-i EMOJI] [-u URL]
                   [-c CHANNEL [CHANNEL ...]]
                   TEXT [TEXT ...]

    A tiny utility to send Slack messages using Incoming WebHook.

    positional arguments:
      TEXT                  parts of message to be merged into one

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         show program's version number and exit
      -n, --name NAME       username for the message, default: `slackme`
      -i, --icon-emoji EMOJI
                            emoji for the massage, default: `rocket`
      -u, --url URL         Hook url which can also be provided via environment
                            variable SLACK_URL
      -c, --channels CHANNEL [CHANNEL ...]

Example usage in Ansible

.. code::

    - name: notify deploy
      when: image|changed or force is defined
      become: false
      local_action: "command slackme
                     --url {{ slack_url }}
                     --name deploy
                     --icon-emoji rocket
                     --channels deploy some-project
                     '`{git_user}` deployed `{{ project_name }}:{{ env_name }}`'
                     'from docker image `{{ docker_image }}`'
                     'to `{{ ansible_user_id }}@{{ inventory_hostname }}`'"
      tags:
        - deploy
