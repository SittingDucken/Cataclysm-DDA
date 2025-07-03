# CDDA_Twison

CDDA_Twison is a format for for [Twine 2](http://twinery.org/2) that exports JSON formatted for CDDA NPC talk-topics.

Twison is a story format for [Twine 2](http://twinery.org/2) that simply exports to JSON.

It is inspired by [Entweedle](http://www.maximumverbosity.net/twine/Entweedle/) as a model for how Twine 2 story formats work.

## Installation

From the Twine 2 story select screen, add a story format, and point it to the url `https://cataclysmdda.org/tools/cdda-twison/dist/format.js`.

From within your story, set the story format to CDDA_Twison. Choosing "Play" will now give you a JSON file.

## Output

Here's an example of its output:

```jsonc
[
  {
    "topic": "talk_topic",
    "tags": [
      "INTRO"
    ],
    "id": "Intro",
    "dynamic_line": "Hey there, stranger! I'm Nautilus, leader of this little caravan we have here. We've got quite a few supplies to deliver, and it looks like you could use some help. Why don't you join us?",
    "responses": [
      {
        "topic": "Cost",
        "text": "What's it going to cost me?"
      },
      {
        "topic": "Backstory",
        "text": "What's your story?"
      }
    ]
  },
  {
    "topic": "talk_topic",
    "tags": [
      "LANDING",
      "EXIT"
    ],
    "id": "Landing",
    "dynamic_line": "Have some more questions? Ask away, and I'll do my best to shed some light.",
    "responses": [
      {
        "topic": "Cost",
        "text": "What's it going to cost me?"
      },
      {
        "topic": "Backstory",
        "text": "What's your backstory?"
      },
      {
        "topic": "TALK_DONE",
        "text": "Let's go"
      }
    ]
  },
  {
    "topic": "talk_topic",
    "id": "Cost",
    "dynamic_line": "Welp, joining the caravan isn't exactly cheap, but I promise it'll be worth every single coin. We've got a lot of mouths to feed and supplies to buy, so we need people who are willing to chip in and help us out.\n\nBut don't worry, I won't ask for everything you have right away.",
    "responses": [
      {
        "topic": "Landing",
        "text": "Here's some cash.",
        "effect": {
          "u_add_var": "dialogue_survivor_cop_talked_to_survivor_cop",
          "value": "yes"
        }
      },
      {
        "topic": "Landing",
        "text": "Okay, that sounds good.",
        "condition": {
          "u_has_item": "money_twenty"
        }
      }
    ]
  },
  {
    "topic": "talk_topic",
    "id": "Backstory",
    "dynamic_line": "Leading a caravan makes more sense than going solo because it's all about teamwork and cooperation, which are crucial for survival in a post-apocalyptic world. By being part of a group, we can protect each other from various threats like roving gangs, portal storms, or the hordes. And who knows? Maybe one day we'll find fellow survivors to join our journey and make it through this tough world together.",
    "responses": [
      {
        "topic": "Landing",
        "text": "Very interesting, thanks."
      }
    ]
  }
]
```

## Capabilities

Additional features have been baked in:

1. Links

- [Links are available via the standard way of linking in Twine 2.](https://twinery.org/wiki/twine2:how_to_create_links) Formatting expects Links to be on a new line along with the text for the response. The line containing the link will then be transformed into a response.
```
Hey there, stranger!  I'm Nautilus, leader of this little caravan we have here.  We've got quite a few supplies to deliver, and it looks like you could use some help.
Why don't you join us?

What's it going to cost me? [[Cost]]
What's your story? [[Backstory]]
```

This text segment becomes:
```jsonc
{
    "topic": "talk_topic",
    "id": "<Name of Story Card>",
    "dynamic_line": "Hey there, stranger!  I'm Nautilus, leader of this little caravan we have here.We've got quite a few supplies to deliver, and it looks like you could use some help.\nWhy don't you join us?",
    "responses": [
        {
            "topic": "Cost",
            "text": "What's it going to cost me?"
        },
        {
            "topic": "Backstory",
            "text": "What's your story?"
        }
    ]
}
```

2. Props

- Props are available by adding them as so to the passage text: "{{foo}}bar{{/foo}}". Props are only supported in a single instance. eg {{condition}}{{u_has_var}}dancing{{/u_has_var}}{{/condition}} works but {{condition}}(same stuff){{/condition}}{{effect}}(new_stuff){{/effect}} doesn't work. 

For instance this text segment of a response line:
```
Here's some cash. [[Landing]] {{effect}}{{u_add_var}}dialogue_survivor_cop_talked_to_survivor_cop{{/u_add_var}}{{value}}yes{{/value}} }{{/effect}}
```
Is exported as
```jsonc
      {
        "topic": "Landing",
        "text": "Here's some cash.",
        "effect": {
          "u_add_var": "dialogue_survivor_cop_talked_to_survivor_cop",
          "value": "yes"
        }
      },
```

1. Tags
- Tags are included for your benefit as reminders. They currently serve no functionallity and need to be deleted before ingesting into CDDA.

## Development

If you want to hack on CDDA_Twison itself:

Go to [CDDA_Twison](https://github.com/SittingDucken/sittingducken.github.io) and follow Development instructions there.

## License

CDDA_Twison is licensed under the MIT license. See the LICENSE file for more information.
