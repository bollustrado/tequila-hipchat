#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
def getfact():
	i=random.randint(0, 8)
	facts=[
			"Tequila Is Plant-Based.Tequila is made from the blue agave, or agave Tequilana Weber. According to WebMD, the core of the plant contains aguamiel or “honey water,” which is used for syrup (and Tequila) production.",
			"Tequila Is Technically A Mezcal. But mezcal is not Tequila. Got that? The main difference between the two is the plant. All Tequila must be produced using blue agave, whereas a variety of agave plants can be used to make a single mezcal batch.",   
			"The Machete Used To Chop Agave Leaves Is Called A Coa. And it has circular blades.", 
			"The Men Who Use The Coa Are Called Jimadors. ",  
			"Only The Agave Heart Is Used To Make Tequila. Tequila is produced by removing the heart, or piña, of the agave plant, which can weigh anywhere from 80 to 200 pounds when harvested. This heart is stripped of its leaves and then cooked to remove the sap, which is fermented and distilled.",    
			"Tequila Does NOT Contain Psychedelic Properties. In the mid-20th century, Tequila sales spiked after California residents thought it was a psychedelic. Nope. They were just confusing mezcal with mescaline (the psychoactive alkaloid of peyote).",    
			"You Can Turn Tequila Into Diamonds. Physicists at the National Autonomous University of Mexico figured out a way to make artificial diamonds out of Tequila. Sadly, the synthetic diamonds are too small to be turned into jewelry, but they can be used for an array of electronic and industrial purposes.",		
			"Serious Tequila Aficionados Generally Don’t Do Shots. Instead, they sip Tequila from a special Tequila glass or brandy snifter. That way, the agave flavors and aromas can be properly enjoyed.",	
			"A Bottle Of Tequila Can Last Unopened For Years. However, once you open a bottle, you have about one to two months before oxidization and evaporation lower the quality of the Tequila and destroys the agave profile. So, you want to drink up within 3 to 6 months, at which point it becomes more like a bourbon."		
			]
	return "Who said Tequila? By the way... %s" % facts[i]

def hello():
		return "Hi! I am tequila bot, I can !ping, !weather, !google, !host, !calc, !create. \n examples: !ping ya.ru, !calc 100+200, !create SuperRoom But remember. Dont say tequila! (lowcased)"