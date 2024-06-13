# Ensure only a talk's speaker and staff can edit the talk

## Scenario

At present any speaker can edit any talk, which obviously isn't the best approach. You've been tasked with updating the site to ensure only the speaker who submitted the talk, and staff, can edit the talk. An issue has already been created for you, which is where you'll start the demo.

### Demo overview

1. Ask GitHub Copilot for information about the project and determine where and how to make the updates.
2. Update `TalkEditView` to ensure only the speaker who submitted the talk, and staff, can edit the talk, using the code from Copilot.
3. Show the updates in the website.
4. Use Code Completion to add a new field to hide the edit button for talks that the user can't edit.
5. Show the updates in the website.
6. Use chat to generate tests for the new functionality.
7. Use Copilot to generate a commit message, and push a new branch.
8. Create a pull request and ask Copilot to generate a pull request summary.

## Step-by-step guide

### Dotcom chat

**Platform**: GitHub.com, in your repository

The first step to updating an application is to understand the existing code, to figure out where your code needs to be placed. If you're new to a project, or simply haven't worked on it in a while, this can be rather daunting, especially in large applications. You can access GitHub Copilot chat in the repository to ask questions about the structure and how it works.

As with all good projects, an issue has been created to inform us of the desired update to the application. Notice how it contains a little additional information about how the update should be shaped, that we should use a *Django mixin* (more on that later).

1. Open [issues](../issues), and the issue associated with making the update to control permissions. Note the text in the issue.

Now that we know what to do, next we have potentially the toughest part - figuring out where to do it. For complex applications, we could spend quite a bit of time clicking around, doing keyword searches, all to find the proverbial needle in the haystack. Fortunately, GitHub Copilot chat right here in the repository can hellp us out. Let's start by just figuring out what the application does.

1. Open chat by selecting the GitHub Copilot icon, and ask **"What does this application do"**
2. Ask **"where do users submit and edit talks?"** and note how you receive both an overview of the implementation and links to the files. Highlight how you were able to ask the question using natural langauge, and GitHub Copilot understood what you were looking for. Attempting to do the same search with keywords would have taken much longer, and may have been fruitless.

Now that we know where the operations take place, we can dig a little deeper to determine exactly what needs to be done and where it needs to happen. Let's open up the **views.py** file and get a little more information.

1. Select the link to **views.py**. Scan through the file, and note the GitHub Copilot icon on the file. Select the icon to continue the conversation, and ask **"What `TalkEditView` do?"**. GitHub Copilot provides a summary of the view, giving even more context.

We've seen how GitHub Copilot can help give me specific information about the application. But it can also answer generic questions about programming. The issue filed highlighted a desire to use a Django mixin. What if it's been a little while since I've used Django and can't remember what it is? Or what if I'm a junior developer, have never seen this before, and don't want to bother anyone. Fortunately, I can just ask Copilot for help.

1. Ask Copilot **"What are Django mixins?"** and review the answer.
2. Ask Copilot **"How could a mixin help with controlling user access to objects?"** and review the answer.

OK, we've got a good understanding of what mixins are, and how they could help. Now let's see what code Copilot thinks we should use to update our application. The big key to note is normally I'd head off to Google or another search engine, find some code, copy/paste, edit, etc. With Copilot I'll receive a bespoke response with my project structure in mind.

1. Ask Copilot **"How can I update TalkEditView to ensure only a talk's speaker and staff can edit the view? Use a mixin to make the update."** Note how the response is custom to this environment, and takes into account the restrictions applied. Copy the code provided, and note that it's time to turn our attention to writing code.

### Code completion

**Platform**: Codespace

Now that we have a good understanding of the application, and the code we need to write, we can make the changes. While it's certainly possible to edit the file directly on GitHub.com, most developers are going to use an IDE. Let's see how this is done. We'll update `TalkEditView` to ensure that only the talk's speaker and staff can edit the view.

Let's open up the views file, and paste in the suggested code.

1. Open the Codespace for the repository. Open **agenda/views.py** and locate `TalkEditView`. Replace the class with the code copied from GitHub Copilot chat from the prior demo.

Now that we've made the update, let's test it. Let's ensure that if we logon as a user, in this case Jamal, that he can only edit his own talks.

1. Open a terminal window by selecting <kbd>Cmd</kbd>+<kbd>\`</kbd>.
2. Run the command `python manage.py runserver` to start the application.
3. Select the link in the website to open the site.
4. Login as **jamal** with a password of **P@ssw0rd**. 
5. Select a talk created by someone other than Jamal. 
6. Notice how the **Edit** button still appears, but that selecting it displays an error.                                               |

OK, we're part of the way there. We can't edit talks we didn't submit, but the edit button still displays. It'd be nice to hide that. In Django the way this is typically accomplished is by adding a field to a view's context, and then accessing this in the HTML template.

It's worth highlighting that Copilot doesn't replace developers; developers should still be familiar with the languages and frameworks they're using to get the most out of the tool.

Let's make the update to ensure the edit button appears only if the user can edit the talk.

1. Return to **views.py** in your IDE.
2. Scroll to the bottom and locate `TalkDetailView`.
3. Tab in one level (you may need to delete some Copilot suggestions here), and prompt Copilot with the following comment:

    ```python
    # Add a context field named can_edit to determine if the user can edit the talk
    ```

4. Accept the suggested by pressing <kbd>Tab</kbd>. Notice the suggestion takes into account the context, and uses the same logic as before.

We've got the view updated; now we need to update the template, which is responsible for actually displaying information to the user.

1. Open **agenda/templates/detail.html**.
2. On or about **line 14**, replace `{% if user.is_authenticated %}` with `{% can_edit %}`.

Let's test the udpate.

1. Return to the website in the browser.
2. Return to the list of talks.
3. Open a talk which Jamal didn't submit, and note the edit button is now gone.
4. Do the same for a talk he did submit, and notice the flow works correctly.

### GitHub Copilot Chat in the IDE

**Platform**: Codespace

We've seen how GitHub Copilot chat can be used to understand the application, and to help write code. But what if we have questions while we're writing the code? We can use GitHub Copilot chat in the IDE to ask questions and get help.

>  **NOTES**: There are a lot of different directions you could go with Chat depending on your comfort level and the level of the audience. You could create documenation, ask questions about the code, create tests, etc. Below is a core example of how to use chat to ask questions about the code. It asks how the class works, and generates tests. The demo doesn't actually run the tests, but you could do that if you wanted to. As always, GitHub Copilot is probabilistic, and the quality of the responses will vary; you may need to make updates to the code or tests generated.

We've already seen how we can access chat on the repository. As you would expect, we can do the same in the IDE. Let's ask a question about the code we just wrote. Let's see if we can get some documentation for it.                                                                    

1. Open **Chat** in the IDE.
2. Highlight the `TalkDetailView`, and ask **"What does this code do?** and walk through the response.

While most every developer knows the importance of writing tests, there aren't many who enjoy the process. It can be tedious and mundane. Fortunately, GitHub Copilot Chat can allow me to offload this. Let's create tests for the `can_edit` flag.

1. With `TalkDetailView` still highlighted, type **/tests** in chat and select <kbd>Tab</kbd> and select <kbd>Return</kbd>.
2. Notice how this creates a set of unit tests for the `can_edit` field.

GitHub Copilot Chat can be a useful learning tool for developers. Notice how after generating tests we are prompted to continue to explore how tests work and run. This also helps developers get more comfortable with GitHub Copilot, showing examples of the types of questions it can answer and actions it can perform.

1. Note the follow-up question provided by chat. Click through a couple, talking about each one.

### Creating commit messages and PR summaries

**Platform:** Codespace and GitHub.com (in your repository)

Now that we've made the updates, it's time to commit the changes and open a pull request. Generally speaking, most developers are out of creative energy at this point, having spent it all on the code. GitHub Copilot can help you write a commit message and pull request description.

Let's create a new branch with our code, stage the changes, and then have GitHub Copilot generate the commit message.

> **NOTE**: The demo uses the IDE when working with commits and branches. You can also use the terminal window in VS Code, which also provides sparkles to help guide you along.

1. Open the **Source Control** view by selecting the icon in the Activity Bar.
2. Select the **...** (ellipsis) > **Branch** > **Create new branch**.
3. Name the branch **control-edits** and press <kbd>Return</kbd>.
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
