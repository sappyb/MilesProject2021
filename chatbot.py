from parlai.scripts.interactive import Interactive
# call it with particular args
Interactive.main(
    # the model_file is a filename path pointing to a particular model dump.
    # Model files that begin with "zoo:" are special files distributed by the ParlAI team.
    # They'll be automatically downloaded when you ask to use them.
    model_file='zoo:blender/blender_90M/model'
)
