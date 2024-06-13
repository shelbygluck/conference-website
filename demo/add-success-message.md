# Display success message

## Scenario

Right now, when a speaker submits or edits a talk, the website returns to the list of talks with no indication of the operation performed. You've been tasked with updating the application to display a success message after a speaker submits or edits a talk. The message should appear at the top of the page, and should be styled as a Bootstrap alert. An issue has been created, and it's where you'll start the demo.

### Demo overview

During the demo, you will:

1. Ask GitHub Copilot for information about the project and determine where to make the updates.
2. Use GitHub Copilot to write the Python in `TalkSubmitView` and `TalkEditView`, and HTML to display the success message.
3. Show the updates in the website.
4. Return to the HTML and ask Chat to generate an update to the HTML code.
5. Use Copilot to generate a commit message, and push a new branch.
6. Create a pull request and ask Copilot to generate a pull request summary.

## Step-by-step guide

### Dotcom Chat

**Platform:** GitHub.com, in your repository

The first step to updating an application is to understand the existing code, to figure out where your code needs to be placed. If you're new to a project, or simply haven't worked on it in a while, this can be rather daunting, especially in large applications. You can access GitHub Copilot chat in the repository to ask questions about the structure and how it works.

Trying to figure out where to make the updates can be rather challenging for a developer who is new to the project, or maybe hasn't worked on it in a while. Fortunately, with GitHub Copilot, you can ask questions in natural language about the project.

1. Open [issues](../issues), and the issue associated with making the update to display success messages. Note the text in the issue.
2. Inside the repository on GitHub.com, select the **Copilot** icon to open chat. Ask **"What does this application do?"**, and explore the results.
3. Ask **"Where are talks submitted and edited?"**. Highlight how you receive an overview of the implementation, and links to the files. Also note how the question didn't use any specific terminology or class names, but GitHub Copilot understood the context of the question and was able to provide results. Performing this same operation with keyword searches would have been much more difficult, if not fruitless.
4. Ask **What is the base template for talks?**. Highlight how Copilot shows the links to the files, and provides information about the base template. Again, we're using natural language here, and able to dive even deeper into the structure of the project.

Now that we know where to perform the updates, let's see what needs to be done. GitHub Copilot can both help me understand my project, but also more generic coding questions. What's wonderful is the answers provided will consider the context of my application.

1. Select **views.py** to open the Views file. Select the **Copilot** icon, and highlight how you're continuing the conversation. Ask **"How do I display a success message after a talk is submitted or edited?"** and now how the answer provides code snippets relevant to your project.
2. Follow up by asking **"How does the Django messaging framework work?"**, and note how you can learn inline about Django, expanding your knowledge as a developer, allowing you to grow.

### Code completion

**Platform:** Codespace

Now that you know where to make the updates, and have an understanding of what needs to be done, it's time to start writing some code. While it could be done in the editor on GitHub.com, most developers will feel more comfortable inside an IDE. Let's open the site in a Codespace and start writing some code.

Based on our conversation with GitHub Copilot, we know we need to make updates to `TalkEditView` and `TalkSubmitView`, and to the HTML template. Let's start by updating the views.

1. If not already done, open the project inside of a Codespace. Open **agenda/views.py**.
2. Inside `TalkSubmitView`, locate the `form_valid` function.
3. Create a new line below `form.instance.speaker = form.request.user`, and add a comment which says `# Add a success message with the name of the talk.`.
4. Select <kbd>Tab</kbd> to accept the new line, and talk about the result.
5. Scroll down to `TalkEditView`, and create a new line below `def form_valid(self, form):`, and add the same comment `# Add a success message with the name of the talk.`.
6. Select <kbd>Tab</kbd> to accept the new line, and talk about the result.

The view is responsible for setting the values to be displayed, while the template is responsible for actually displaying the message. Let's update the base template to display any messages from Django.

1. Open **agenda/templates/base.html**.
2. In the empty space below `</section>`, add a new Django comment to ask Copilot to display messages:

    ```django
    {# Display messages from Django in a Bootstrap alert #}
    ```

3. Select <kbd>Tab</kbd> to accept the new line, and talk about the result. Note how it's using Bootstrap to use the [Alert component](https://getbootstrap.com/docs/4.0/components/alerts/).

Now that we've got the code updated, let's test the updated page. Let's launch the site, login as a user, and edit a value.

1. Open the terminal by pressing <kbd>Cmd</kbd>+<kbd>\`</kbd> and run the following command to start the server:

    ```bash
    python manage.py runserver
    ```

2. Select the link in the terminal window to open the site in the browser.
3. Login as a user, and edit a talk. You should see a success message at the top of the page. Notice, however, that you can't dismiss the alert.

Software development is always iterative. GitHub Copilot gave us a correct answer, but we didn't give it enough context to know that we wanted to dismiss the alert. Let's ask Copilot how to dismiss the alert.

1. Open **agenda/templates/base.html**.
2. Select the entire block of HTML and comment generated in the previous step.
3. Open Copilot Chat and ask **"How do I make a Bootstrap alert dismissible?"**.
4. Use the **Insert at cursor** button to insert the code into the file.
5. Return to the browser and refresh the page. Edit another talk and notice that the alert is now dismissible.

### Commit message and pull requests

**Platform:** Codespace and GitHub.com (in your repository)

Now that we've made the updates, it's time to commit the changes and open a pull request. Generally speaking, most developers are out of creative energy at this point, having spent it all on the code. GitHub Copilot can help you write a commit message and pull request description.

Let's create a new branch with our code, stage the changes, and then have GitHub Copilot generate the commit message.

> **NOTE**: The demo uses the IDE when working with commits and branches. You can also use the terminal window in VS Code, which also provides sparkles to help guide you along.

1. Open the **Source Control** view by selecting the icon in the Activity Bar.
2. Select the **...** (ellipsis) > **Branch** > **Create new branch**.
3. Name the branch **add-success-message** and press <kbd>Return</kbd>.
4. Mouse over **Changes**, then select the **+** to stage all changes.
5. Select the **Sparkles** icon in the **Message** box to have Copilot generate the commit message.
6. Select **Commit** to commit the changes.
7. Select **Publish branch** to push the branch to GitHub.

With the commit message created and the new branch pushed, let's create the pull request and summarize our work.

1. Return to your repository in GitHub.com.
2. Select **Compare & pull request** from the alert window.
3. Select the **Copilot** icon, then **Summary** to have Copilot generate the pull request description.
4. Select **Create pull request** to open the pull request.

Notice how Copilot summarized all changes made, including links to the files and the code changes. This is a great way to ensure that your pull request is informative and easy to understand.

## Summary

Throughout the process, GitHub Copilot was there to support me as the developer. It helped me understand the project, to figure out where to perform the necessary updates and how to perform them. It helped me write the code in the editor, to create the tests, and to create a good commit message. Finally it summarized everything for me for the pull request. Writing code isn't just about writing code; it's about understanding the problem, and then documenting the solution. GitHub Copilot was there to help me every step of the way.