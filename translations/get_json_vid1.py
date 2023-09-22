import re
import json

# Provided chapter text
chapter_text = """Chapters:
00:00:00 intro
00:00:25 micrograd overview
00:08:08 derivative of a simple function with one input
00:14:12 derivative of a function with multiple inputs
00:19:09 starting the core Value object of micrograd and its visualization
00:32:10 manual backpropagation example #1: simple expression
00:51:10 preview of a single optimization step
00:52:52 manual backpropagation example #2: a neuron
01:09:02 implementing the backward function for each operation
01:17:32 implementing the backward function for a whole expression graph
01:22:28 fixing a backprop bug when one node is used multiple times
01:27:05 breaking up a tanh, exercising with more operations
01:39:31 doing the same thing but in PyTorch: comparison
01:43:55 building out a neural net library (multi-layer perceptron) in micrograd
01:51:04 creating a tiny dataset, writing the loss function
01:57:56 collecting all of the parameters of the neural net
02:01:12 doing gradient descent optimization manually, training the network
02:14:03 summary of what we learned, how to go towards modern neural nets
02:16:46 walkthrough of the full code of micrograd on github
02:21:10 real stuff: diving into PyTorch, finding their backward pass for tanh
02:24:39 conclusion
02:25:20 outtakes :)"""

# Regular expression to match time and chapter title
pattern = r"(\d+:\d+:\d+)\s+(.*)"

# Find all matches
matches = re.findall(pattern, chapter_text)

# Create chapters list
chapters = []
for start_time, title in matches:
    h, m, s = map(int, start_time.split(":"))
    start_time_seconds = h * 3600 + m * 60 + s
    chapters.append({
        "title": title.replace(" ", "_").replace("#", "_").replace(":", "_").replace(",", "_"),
        "start": start_time_seconds
    })

# Convert to JSON
chapters_json = json.dumps(chapters, indent=4)

print(chapters)