# Demo overview and setup

## Scenario

The demo application is written in Python [Django](https://www.djangoproject.com/), and is built to be a sample app for a conference. The app allows users to register, to submit and edit talks, and to list all talks. It's designed to demonstrate how developers would use GitHub Copilot to write code using a framework.

Two demos are provided for you to walk customers through; each covers the same range of topics. You can choose the demo you feel most comfortable with.

## Technical prerequisites

The demo assumes you are comfortable with Python and HTML. Familiarity with [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) and Django will help, but aren't necessarily required. There are [two scenarios](#step-by-step-guide) to choose from, based on your comfort level.

> **NOTE:** If you wish to learn more about Django, the [official tutorial](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) is a great place to start, and will take about 30 minutes to walk through.

## System requirements

This demo is designed to be self-contained, and to be run in a Codespace. The default Codespace, which includes Python, is sufficient to run the demo.

1. Create a [new repository via the template](https://github.com/new?owner=octodemo&template_name=geektrainer-demo-conference&template_owner=octodemo).
2. Open the repository in a Codespace, ensuring it's in a new tab.
3. Open a new terminal in the Codespace by selecting <kbd>Cmd</kbd>+<kbd>\`</kbd> (or <kbd>Ctrl</kbd>+<kbd>\`</kbd> on a PC).
4. Install the required Python packages by running the following command:

    ```bash
    pip install -r requirements.txt
    ```
5. Create the database by running the following command and following the prompts:

    ```bash
    python manage.py setup-demo
    ```

    The [setup script](../demo_setup/management/commands/setup-demo.py) will prompt you for a username, email, and password for the admin user. It will then create the database and populate it with some sample data, including a few talks and a few users.

6. Create the issues used by the demo by running the following commands:

    ```bash
    gh issue create --title "Add success messages" --body "Display a success message with the title when a speaker submits or edits a talk."
    gh issue create --title "Limit edits to staff or talk's speaker" --body "We need to ensure only staff or a talk's speaker can edit a talk. Using a Django mixin is probably the best approach here." 
    ```

## Step-by-step guide

Two guides are provided for you to choose from. They are leveled based on your experience with Django, and you can decide the level of depth you want to demonstrate. Both demos walk through the same concepts about GitHub Copilot.

- [Add success messages](./add-success-message.md): You will update the application to display status messages, which appear after a speaker submits or edits a talk. The demo uses the [messages framework](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/) and [Bootstrap alerts](https://getbootstrap.com/docs/4.0/components/alerts/). You will ask GitHub Copilot for information about the project and perform the task. You'll then make the appropriate updates (two lines of Python code, and a little bit of enhanced HTML). After showing the updates were successful, you'll use Copilot to generate a commit message and PR summary. GitHub Copilot does a great job with this scenario, and will write basically everything for you. This demo assumes little to no familiarity with Django, and will take about 15 minutes to walk through. You should be comfortable:
  - Writing Python code; you will add 2 lines of Python code to the project.
  - Writing HTML; you will add a few lines of HTML to the project.
- [Control editing of talks](./control-talks.md): You will update the application to ensure speakers can only edit their own talks, and that staff can edit all talks. You'll ask GitHub Copilot where talks are edited and submitted, how to make the changes, and eventually make the necessary updates. You'll work iteratively across a couple of files, and generate about 6 lines of Python code and one line of HTML. You'll want to be familiar with [Django mixins](https://docs.djangoproject.com/en/5.0/topics/class-based-views/mixins/). The demo will take about 20 minutes to walk through. You should be comfortable:
  - Writing Python code; you will add several lines of Python code to the project.
  - Working with Django mixins; you will add and work with the `UserPassesTestMixin`.
  - Writing HTML; you will add a line of HTML to the project.
