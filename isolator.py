from Trainer import trainer
# import Analyzer

if __name__ == "__main__":
    '''python isolator.py'''
    options = {}

    options["input_data"] = "/public/data/RNN/lepton_track_data.pkl"
    options["output_folder"] = "Outputs/Test/"

    options["RNN_type"] = "RNN"
    options['learning_rate'] = 0.0001
    options['training_split'] = 0.7
    options['batch_size'] = 100
    options['n_batches'] = 50
    options['n_layers'] = 5
    options['hidden_neurons'] = 128
    options['output_neurons'] = 2
    options['bidirectional'] = False

    trainer.train(options)