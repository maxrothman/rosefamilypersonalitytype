# Rose Family Personality Type Generator
## An Internet Quiz

Generates a type judging by who you are most like in
descending order. 

Johnny
Moira
David
Alexis

Character Stats (stored in JSON?)

Lovability
Selfishness
Lovable Selfishness
Entrepeneurship
Modesty
Entitlement
Wit

ask questions which may:
	assign numbers to your character quotients

at the end, all question results are averaged

you end up with a stat page, like the characters?

how does it order which characters you are closest to?

there will have to be an order of operations.

HOW DO I QUANTIFY CHARACTER CLOSENESS?

7 different stats, each on a scale of 1-10

* each stat is subtracted from yours
* negative numbers are turned positive
* numbers are added together
* smallest numbers get the highest closeness scores

multiple choice questions give you specific stat quotients

how do I store questions? It'd be nice to be able to easily
add questions. so they should be in a standard format.

JSON!

{
	"question": "wwwww?",
	"answer a":{ "lovability":4 ,"selfishness":7 }
	"answer b":{ "lovable selfishness":10, "modesty":2 }
	# etc
}
