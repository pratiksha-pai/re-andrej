import os
from pydub import AudioSegment
chapters = [
    {
        "title": "intro",
        "start": 0
    },
    {
        "title": "micrograd_overview",
        "start": 25
    },
    {
        "title": "derivative_of_a_simple_function_with_one_input",
        "start": 488
    },
    {
        "title": "derivative_of_a_function_with_multiple_inputs",
        "start": 852
    },
    {
        "title": "starting_the_core_Value_object_of_micrograd_and_its_visualization",
        "start": 1149
    },
    {
        "title": "manual_backpropagation_example__1__simple_expression",
        "start": 1930
    },
    {
        "title": "preview_of_a_single_optimization_step",
        "start": 3070
    },
    {
        "title": "manual_backpropagation_example__2__a_neuron",
        "start": 3172
    },
    {
        "title": "implementing_the_backward_function_for_each_operation",
        "start": 4142
    },
    {
        "title": "implementing_the_backward_function_for_a_whole_expression_graph",
        "start": 4652
    },
    {
        "title": "fixing_a_backprop_bug_when_one_node_is_used_multiple_times",
        "start": 4948
    },
    {
        "title": "breaking_up_a_tanh__exercising_with_more_operations",
        "start": 5225
    },
    {
        "title": "doing_the_same_thing_but_in_PyTorch__comparison",
        "start": 5971
    },
    {
        "title": "building_out_a_neural_net_library_(multi-layer_perceptron)_in_micrograd",
        "start": 6235
    },
    {
        "title": "creating_a_tiny_dataset__writing_the_loss_function",
        "start": 6664
    },
    {
        "title": "collecting_all_of_the_parameters_of_the_neural_net",
        "start": 7076
    },
    {
        "title": "doing_gradient_descent_optimization_manually__training_the_network",
        "start": 7272
    },
    {
        "title": "summary_of_what_we_learned__how_to_go_towards_modern_neural_nets",
        "start": 8043
    },
    {
        "title": "walkthrough_of_the_full_code_of_micrograd_on_github",
        "start": 8206
    },
    {
        "title": "real_stuff__diving_into_PyTorch__finding_their_backward_pass_for_tanh",
        "start": 8470
    },
    {
        "title": "conclusion",
        "start": 8679
    },
    {
        "title": "outtakes__)",
        "start": 8720
    }
]

# Create a folder to store the sliced audio files
output_folder = "/home/hice1/ppai33/scratch/sliced_audio"
os.makedirs(output_folder, exist_ok=True)

audio = AudioSegment.from_wav("/home/hice1/ppai33/scratch/karpathy_english.wav")
for i in range(len(chapters)):
    start_time = chapters[i]['start'] * 1000  
    try:
        end_time = chapters[i + 1]['start'] * 1000
    except IndexError:
        end_time = len(audio) * 1000
    
    slice = audio[start_time:end_time]
    print(start_time, end_time)
    slice.export(os.path.join(output_folder, f"slice_{i}.wav"), format="wav")
