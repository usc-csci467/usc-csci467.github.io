---
layout: class
title: "CSCI 467: Introduction to Machine Learning"
semester: Fall 2023
time: Tuesdays and Thursdays at 2:00-3:20pm
location: LVL 17
location_link: "https://maps.usc.edu/?id=1928&reference=LVL"
section_time: Fridays at 2:00-2:50pm
section_location: DMC 100
section_location_link: "https://maps.usc.edu/?id=1928&reference=DMC"
instructor: Robin Jia
order: 1
---
<div class="row" markdown=1>
<div class="col-pic" markdown=1>
![xkcd Tasks](https://imgs.xkcd.com/comics/tasks.png)
Source: [xkcd](https://xkcd.com/1425/)
</div>
<div class="col-intro" markdown=1>


**Quick Links:**
* **[Lecture Notes](assets/notes.pdf)** (will be continuously updated throughout the semester)

{::comment}
* **[Final Project information](project)**
{:/comment}


**News:**   
* Homework 0 has been released ([pdf](assets/hw0.pdf), [code](assets/hw0.zip))!
It is due **Thursday, August 31**.

Some problems in computer science admit precise algorithmic solutions.
Checking if someone is in a national park is, in some sense, straightforward:
get the user's location,
get the boundaries of all national parks,
and check if the user location lies within any of those boundaries.

Other problems are less straightforward.
Suppose you want your computer to determine if an image contains a bird.
To your computer, an image is just a matrix of red, green, and blue pixels.
How do you even begin to write the function `is_bird(image)`?

For problems like this, we turn to a powerful family of methods known as **machine learning.**
The zen of machine learning is the following:
1. I don't know how to solve my problem.
2. But I can obtain a **dataset** that describes what I want my computer to do.
3. So, I will write a program that **learns the desired behavior from the data.**

This class will provide a broad introduction to machine learning.
We will start with **supervised learning,** where our goal is to learn an input-to-output mapping given a set of correct input-output pairs. 
Next, we will study **unsupervised learning,** which seeks to identify hidden structure in data.
Finally, we will cover **reinforcement learning,** in which an agent (e.g., a robot) learns from observations it makes as it explores the world.

</div>
</div>

## Course Staff
<div class="staff-photo" markdown=1>
![Robin Jia](//robinjia.github.io/assets/images/profile.jpg)  
**Robin Jia**  
Instructor
</div>
<div class="staff-photo" markdown=1>
![Soumya Sanyal](/assets/images/soumya.jpg)  
**Soumya Sanyal**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Wang (Bill) Zhu](//billzhu.me/author/admin/avatar_hu42410483742cac5c8006d54d4d8d8fd3_63927_250x250_fill_q90_lanczos_center.jpg)  
**Wang (Bill) Zhu**  
Teaching Assistant
</div>
<div class="staff-photo" markdown=1>
![Vishesh Agrawal](/assets/images/vishesh.jpg)  
**Vishesh Agrawal**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Ryan Wang](/assets/images/ryan.jpg)  
**Ryan Wang**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Lorena Yan](/assets/images/lorena.jpg)  
**Lorena Yan**  
Course Producer
</div>
<div class="staff-photo" markdown=1>
![Wenyang Zhang](/assets/images/wenyang.jpg)  
**Wenyang Zhang**  
Course Producer
</div>

## Logistics
* **Office hours**: See [calendar](https://calendar.google.com/calendar/embed?src=c_86e4982ab98a1b157f078d62c4489999c4833f08ae66003b169896dd26cca926%40group.calendar.google.com&ctz=America%2FLos_Angeles).
* **Assignments**: Assignments should be submitted through [Gradescope](https://www.gradescope.com/courses/577750). Feedback will also be provided on Gradescope. All enrolled students should be in Gradescope automatically--let me know if you are not!
You should submit both your PDF writeup and your code on Gradescope; there will be separate assignments for each.
* **Discussions**: We will be using Piazza for general course-related questions and announcements. 
All enrolled students were added at the beginning of the semester; you can also use this [sign-up link](https://piazza.com/usc/fall2023/csci467).
If you have an individual matter to discuss, email me directly (please put "CSCI 467" in the subject line) or come to my office hours. For grading questions, go to the office hours of the person who graded the problem in question.

## Prerequisites
* Algorithms: CSCI 270 
* Linear Algebra: MATH 225 
* Probability: EE 364 or MATH 407 or BUAD 310

This class will also use some basic multivariate calculus (taking partial derivatives and gradients).
However, knowledge of single-variable calculus is sufficient as we will introduce the required material during class and section. 


## Schedule
All assignments are due by **11:59pm** on the indicated date.

|Date|Topic|Related Readings|Assignments|
|--|--|--|--|
|Tue Aug 22|Introduction ([slides](assets/lectures/01_intro.pdf)) |PML 1| Homework 0 released ([pdf](assets/hw0.pdf), [code](assets/hw0.zip)) |
|Thu Aug 24|Linear Regression ([lecture](assets/lectures/02_linreg.pdf), [demo](https://colab.research.google.com/drive/11hdXd0C7GGrxpJlC-PV6eImcWJ3Bk_Q2?usp=sharing)) |PML 7.8, 8.2|
|Fri Aug 25|Section: Probability, Linear Algebra, & Calculus Review [Soumya] ([handout](https://hackmd.io/@charlotteTYC/prerequisites){: .schedule-section}, [notes](assets/lectures/section1_notes.pdf)) | |
|Tue Aug 29|Featurization, Convexity, Maximum Likelihood Estimation ([lecture](assets/lectures/03_linreg2.pdf)) |PML 2.6.3, 4.2, 8.1 ||
|Thu Aug 31|Logistic Regression, Softmax Regression |PML 10.1-10.3| **Homework 0 due** |
|Fri Sep 1|Section: Python & numpy tutorial [Bill] ([colab](https://colab.research.google.com/drive/1Qe_HXHHD2KyvOZbbXyl-ly2zSmD_qucp?usp=sharing){: .schedule-section}) | | 
|Tue Sep 5|Overfitting, Regularization, Bias and Variance|PML 4.5, 4.7, 11.3-11.4 |
|Thu Sep 7|Normal Equations, Second-order optimization | PML 8.3, 11.2| Homework 1 released |
|Fri Sep 8|Section: Probability review continued, taking gradients [Soumya] [](){: .schedule-section}| | 
|Tue Sep 12| Generative Classifiers, Naive Bayes  |PML 9.3-9.4 |
|Thu Sep 14 |Nearest Neighbors, Project discussion |PML 16.1, 16.3 |
|Fri Sep 15|Section: Cross-Validation, Evaluation Metrics  [Bill] ([slides](assets/sections/section3.pdf){: .schedule-section}) | | 
|Tue Sep 19 |Kernel methods |PML 4.3, 17.1, 17.3| **Homework 1 due** |
|Thu Sep 21|Introduction to Neural Networks, Dropout, Early Stopping |PML 13.1-13.3 | Homework 2 released |
|Fri Sep 22| Section: Scikit-learn tutorial [](){: .schedule-section}| | 
|Tue Sep 26|Backpropagation |PML 13.4-13.5 | **Project Proposal due** |
|Thu Sep 28|Convolutional Neural Networks |PML 14.1-14.2 |
|Fri Sep 29|Section: Pytorch tutorial [](){: .schedule-section}| | 
|Tue Oct 3|Recurrent Neural Networks |PML 15.1-15.2 |
|Thu Oct 5|Sequence-to-sequence, Attention |PML 15.1-15.2 | **Homework 2 due** |
|Fri Oct 6 |Section: Midterm preparation [](){: .schedule-section}| | 
|Tue Oct 10 |**In-class Midterm Exam** [](){: .schedule-exam} | | 
|Oct 12-13|No class or section (Fall break) [](){: .schedule-break}| |
|Tue Oct 17 |Transformers, Pretraining |PML 15.4-15.7| |
|Thu Oct 19 |Decision Trees, Ensembling |PML 18.1-18.5 |
|Fri Oct 20|Section: Midterm Exam Discussion [](){: .schedule-section}| | 
|Tue Oct 24|k-Means Clustering, Start of Gaussian Mixture Models |PML 21.3 | Homework 3 released
|Thu Oct 26|Gaussian Mixture Models, Expectation Maximization | PML 21.4, PML2 8.1-8.2| 
|Fri Oct 27|Section: Optimization strategies for neural networks [](){: .schedule-section}| 
|Tue Oct 31|Dimensionality Reduction, Principal Component Analysis |PML 20.1, 20.4 |**Project Midterm Report due** |
|Thu Nov 2 |Embedding models, Word Vectors |PML 20.5 |
|Fri Nov 3 |Section: Practical guide to pretrained language models [](){: .schedule-section}| | 
|Tue Nov 7 |Multi-Armed Bandits | PML2 34.1-34.4 | **Homework 3 due**
|Thu Nov 9|Markov Decision Processes, Reinforcement Learning |PML2 34.5-34.6, 35.1, 35.4 | |
|Fri Nov 10|Section: Practical guide to computer vision models [](){: .schedule-section}| | 
|Tue Nov 14|Q-Learning with Function Approximation, Policy Gradient |PML2 35.2-35.3 | Homework 4 released|
|Thu Nov 16|Robustness, Adversarial Examples, Spurious Correlations  |PML2 19.1-19.8 |
|Fri Nov 17|Section: Final Exam preparation [](){: .schedule-section}| | 
|Tue Nov 21|Fairness in Machine Learning | FAML 1-4 | 
|Nov 23-24|No class or section (Thanksgiving) [](){: .schedule-break}| |
|Tue Nov 28|How does ChatGPT work?  | 
|Thu Nov 30|Conclusion | | **Homework 4 due** |
|Fri Nov 31|No section (End of class) [](){: .schedule-break}| | 
|Thu Dec 7|**Final Exam, 2-4pm** [](){:.schedule-exam} | | **Project Final Report due Dec 12**|
{: .schedule #schedule-table}

## Grading
Grades will be based on homework assignments (40%), a class project (20%), and two exams (40%).

**Homework Assignments (40% total)**:
- Homework 0: 4%
- Homeworks 1-4: 9% each

**Final Project (20% total)**.
The final project will proceed in three stages:
- Project proposal: 2%
- Midterm report: 3%
- Final project report: 15%

**Exams (40% total)**:
- In-class midterm: 15% 
- Final exam (cumulative): 25%

### Late days
You have **6 late days** you may use on any assignment **excluding the Project Final Report.**
Each late day allows you to submit the assignment 24 hours later than the original deadline.
You may use a maximum of **3 late days per assignment.**
If you are working in a group for the project, submitting the project proposal or midterm report one day late means that **each member** of the group spends a late day.
We do not allow use of late days for the final project report because we must grade the projects in time to submit final course grades.

If you have used up all your late days and submit an assignment late, you will lose 10% of your grade on that assignment for each day late.
We will **not accept any assignments more than 3 days late.**


## Final project
The final project can be done individually or in groups of up to 3.
This is your chance to freely explore machine learning methods and how they can be applied to a task of our choice.
You will also learn about best practices for developing machine learning methods---inspecting your data, establishing baselines, and analyzing your errors.
More information about the final project will be released at a later date. 

{::comment}
A list of example projects is now available at [here](project).
{:/comment}

## Resources
While there is no required textbook for this class, you may find the following useful:
- [*Probabilistic Machine Learning: An Introduction*](https://probml.github.io/pml-book/book1.html) (PML) and [*Probabilistic Machine Learning: Advanced Topics*](https://probml.github.io/pml-book/book2.html) (PML2) by Kevin Murphy. You may also find PML Chapters 2-3 and 7 useful for reviewing prerequisites.
- [*The Elements of Statistical Learning*](https://hastie.su.domains/Papers/ESLII.pdf) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman.
- [*Patterns, Predictions, and Actions: A Story about Machine Learning*](https://mlstory.org/) by Moritz Hardt and Benjamin Recht
- [*Fairness and Machine Learning: Limitations and Opportunities*](https://fairmlbook.org/) (FAML) by Solon Barocas, Moritz Hardt, and Arvind Narayanan.

To review mathematical background material, you may also find the following useful:
- Probability: [*Introduction to Probability*](http://probabilitybook.net/) by Joseph Blitzstein and Jessica Hwang. Most relevant reading: Chapters 1-5, 7, 9-10.
- Linear Algebra: [*Introduction to Applied Linear Algebra*](https://web.stanford.edu/~boyd/vmls/vmls.pdf) by Stephen Boyd and Lieven Vandenberghe. Most relevant reading: Chapters 1-3, 5-8, 10-11. (Chapters 4 and 12-14 overlap with content for this class.) 
- Multivariate Calculus: [Oliver Knill's lecture notes](https://abel.math.harvard.edu/~knill/teaching/math21a2012/21a_fall_2012.pdf).

## Other Notes
**Collaboration policy and academic integrity**: Our goal is to maintain an optimal learning environment. You may discuss the homework problems at a high level with other students, but you should not look at another student's solutions. Trying to find solutions online or from any other sources for any homework or project is prohibited, will result in zero grade and will be reported. Using AI tools to automatically generate solutions to written or programming problems is also prohibited. To prevent any future plagiarism, uploading any material from the course (your solutions, quizzes etc.) on the internet is prohibited, and any violations will also be reported. Please be considerate, and help us help everyone get the best out of this course.

Please remember the expectations set forth in the [USC Student Handbook](https://policy.usc.edu/studenthandbook/). General principles of academic honesty include the concept of respect for the intellectual property of others, the expectation that individual work will be submitted unless otherwise allowed by an instructor, and the obligations both to protect one's own academic work from misuse by others as well as to avoid using another's work as one's own. All students are expected to understand and abide by these principles. Suspicion of academic dishonesty may lead to a referral to the [Office of Academic Integrity](https://academicintegrity.usc.edu/) for further review.

**Students with disabilities**: Any student requesting academic accommodations based on a disability is required to register with Disability Services and Programs (DSP) each semester. A letter of verification for approved accommodations can be obtained from DSP. Please be sure the letter is delivered to the instructor as early in the semester as possible.
