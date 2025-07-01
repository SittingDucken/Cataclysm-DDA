Need monstergroup?
Each map/event should be defined as a map_card, keeping all the map information in one location.
If needed, separate out common used groups.
map_cards should then have a structure of "card_name/*.json"
hospital_quiet
 -mapgen.json
 -eoc.json
 -items.json
 -monstergroup.json
 -mission.json

With the basic flow being the player chooses a card in the talk menu, the card generates the necessary items/map, gives the player a mission, and then teleports them and their caravan to the location. Need a check for vehicle health and if they can continue in the caravan. For now, the caravan is likely going to just be the PC, NPC, and any allied animals. Teleporting a vehicle I think is probably difficult. 
Need to make a generic EOC for that. Probably start with a single vehicle allowed. 

Roadmap - Minimal Product 
- Avatar with a starting city and an end city.
- Map cards generated in between locations

Roadmap - First Extras
- Map cleanup of previous cards
- PC | NPC | Pet teleport