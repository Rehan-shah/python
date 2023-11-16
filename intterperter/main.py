input = """
card child_marriage
  title "Child marriage"
  text "It’s the end of the year- there is an annual performance and the girls in the 4th are super active and enthusiastic"
  choice "Procced" -> new_classroom

var response
var effectivness

card new_classroom 
  title "New year , New classroom situation" 
  text "It’s a new academic year. While you recognize most of the children in the room you don’t know their backgrounds. what do you do at the start of the year to bond with the children? "
  input "Please enter what will you do" -> {response}
  choice "Procced" -> rate_effectivness

card rating_effectivness
  title "Rating the effectiness"
  text "This is {response} , How effective are these practices to help you bond with the children?"
  choice "very effective" -> {effectiness = 3}
  choice "effective" -> {effectiness = 2}
  choice "not effective" -> {effectiness = 1}
  choice "Procced" -> alternate_action

card alternate_action
  title "Alternate actions" 
  text "Your methhod effectiness is {effectivness} , What other method would use to bond with students"
  input "Please enter other way that you can use to bond with students" 
  choice "Procced" -> interacting_with_studentt

var student_name

card interacting_with_student
  title "Inttecting with student"
  text "During the interactions you find out that a young girl loves reading, she frequently reads about Gandhiji, and wants to become a doctor in the future."
  input "What would like the student name to be" -> {student_name}
  choice "Procced" -> 

card interacting_with_class 
  title "Interacting with class"
  text "It’s a new academic year and you are doing introductions in the classroom ,Some children are open, some are shy, and some are enthusiastic about studying,"
  input "Please enter the action you will do in this scenario"
  choice "Procced" -> answer_interacting_with_class

card answer_interacting_with_class
  title "Answer for interacting with class"
  text "Do do an exercise with the class to examine their notions around speaking up in front of the group, As a teacher you play an important role in maintaining a sense of agency among students, whether shy or enthusiastic is key"
  choice "Next phase" -> 

card Phase_1_intro 
  title "Phase one introduction" 
  text "You assigned important HW for the weekend. Most students completed it except 5 and {student_name}, who usually did her HW"
  choice "Give the rest of the class some work to do and call the child to the front of the room to speak with her" -> choice_1
  choice "Reprimand all the children that have forgotten their HW. And ask them to complete their HW by tomorrow." -> choice_2
  choice "Write a note to the parents of all children and ask them to complete the HW by tomorrow" -> choice_3
  choice "You see {student_name} raise her hand and decided to temper your frustration. You ask all children to complete the HW by tomorrow and let this one instance go." -> choice_4

 
card choice_1 
  title "Option : talk witth child personally"
  text "What do you tell the child ,please select form option below"
  choice "Emphasise the importance of education ,The child keeps quiet and nods their head."
  choice "Convey that it is very unlike her to not complete her HW ,The child keeps quiet and nods their head." 
  choice "Ask calmly and reassuringly- \" Why didn’t you do your HW\"" -> futher_probing
  choice "You will do your HW next time and come, right? The child keeps quiet and nods their head."
  choice "Procced" -> student_reaction



card futher_probing
  title "Your reacting to the child's reactin"
  text "The child doesn’t say anything and just has her head down. Rember Non-judgmental probes can enhance understanding of a child, but excessive probing may harm their self-esteem. Context determines the appropriate approach."
  choice "You say \"I just want to better understand why you didn’t do your HW\" , The child replies I will do it next time"
  choice "Let it be – you see that child is genuinely sad and you let her be."
  choice "Procced" -> student_reaction
"""

json = []


input = input.split("\n")

for n in range(len(input)):
    if input[n].startswith("card"):
        if input[n+1].startswith("  title"):
            title = input[n+1][8:]
        if input[n+2].startswith("  text"):
            text = input[n+2][7:]
        json.append({"line number": n, "title": title, "text": text})


print(json[0]['title'])
