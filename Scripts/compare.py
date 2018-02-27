import pickle
import matplotlib.pyplot as plt
import numpy as np

###################
# Comparison code #
###################

def compareFeatures(inFile, saveDir):

    # load data and get feature index dictionaries
    data = open(inFile)
    data = pickle.load(data)
    [lep_feature_dict, track_feature_dict] = data[0]
    data.pop(0)

    # separate lepton types
    isolated_leptons = [lepton for lepton in data if lepton[lep_feature_dict['lep_isolated']]==1]
    HF_leptons = [lepton for lepton in data if lepton[lep_feature_dict['lep_isolated']]==0]

    # plot comparisons for all lepton features
    for feature, index in lep_feature_dict.items():
        if feature == 'lep_associated_tracks':
            continue
        isolated_feature_values = [lepton[index] for lepton in isolated_leptons]
        HF_feature_values = [lepton[index] for lepton in HF_leptons]
        all_feature_values = isolated_feature_values + HF_feature_values
        bins = np.linspace(min(all_feature_values), max(all_feature_values), 30)
        plt.hist([isolated_feature_values, HF_feature_values], normed=True, bins=bins, histtype='step')
        plt.title(feature)
        plt.legend(['isolated', 'HF'])
        plt.savefig(saveDir + feature + ".png", bbox_inches='tight')
        plt.clf()

    # plot comparisons for calculated and stored ptcone features
    ptcone_features = [
        ("lep_ptcone20", "lep_calculated_ptcone20"),
        ("lep_ptcone30", "lep_calculated_ptcone30"),
        ("lep_ptcone40", "lep_calculated_ptcone40"),
        # ("lep_topoetcone20", "lep_calculated_topoetcone20"),
        # ("lep_topoetcone30", "lep_calculated_topoetcone30"),
        # ("lep_topoetcone40", "lep_calculated_topoetcone40"),
        ("lep_ptvarcone20", "lep_calculated_ptvarcone20"),
        ("lep_ptvarcone30", "lep_calculated_ptvarcone30"),
        ("lep_ptvarcone40", "lep_calculated_ptvarcone40")]
    for feature, calc_feature in ptcone_features:
        lepton_feature_values = [lepton[lep_feature_dict[feature]] for lepton in data]
        lepton_calc_feature_values = [lepton[lep_feature_dict[calc_feature]] for lepton in data]
        plt.scatter(lepton_feature_values, lepton_calc_feature_values)
        plt.title(feature + ' vs. ' + calc_feature)
        plt.xlabel(feature)
        plt.ylabel(calc_feature)
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        plt.savefig(saveDir + feature + "_vs_" + calc_feature + ".png", bbox_inches='tight')
        plt.clf()

#################
# Main function #
#################

if __name__ == "__main__":
    inFile = "/afs/cern.ch/work/m/mazhang/LepIso/Pkl/393407.pkl"
    saveDir = "/afs/cern.ch/user/m/mazhang/Projects/LepIso/LeptonIsolation/Plots/"
    compareFeatures(inFile, saveDir)
