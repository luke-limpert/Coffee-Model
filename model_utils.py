import pandas as pd
import json

class Model_Utils(object):
    """Model Utilities developed by SDI for usage with SimPy"""
    def Minutes(x):
        """When working in seconds, this converts all units of time for use with env.timeout()"""
        """"""
        """Example: yield env.timeout(Model_Utils.Minutes(1))"""
        """This will return 60 time units"""
        """User should specify the number of days they want to represent"""
        return x * 60
    def Hours(x):
        """When working in seconds, this converts all units of time for use with env.timeout()"""
        """"""
        """Example: yield env.timeout(Model_Utils.Hours(1))"""
        """This will return 3,600 time units"""
        """User should specify the number of days they want to represent"""
        return x * 60 * 60
    def Days(x):
        """When working in seconds, this converts all units of time for use with env.timeout()"""
        """"""
        """Example: yield env.timeout(Model_Utils.Days(1))"""
        """This will return 86,400 time units"""
        """User should specify the number of days they want to represent"""
        return x * 60 * 60 * 24
    def create_failure_dictionary(failure_file):
        """Create a dictionary of failures with a text input file"""
        """Using the extend sim database tool, you can select the table to create a text file."""
        """This function will take the text table and convert it into a json file to create a failure dictionary."""
        names = "Cause Name	Failure Type	Initialize	Prob Restart	Product Usage	Distrib (UT)	Param1 (UT)	Param2 (UT)	Prob Stop	Distrib (SDT)	Param1 (SDT)	Param2 (SDT)	Prob (LDT)".split("\t")
        df = pd.read_csv(failure_file, delimiter="\t", header=None, names=names)
        new_columns = df["Cause Name"].to_list()
        df = df.pivot_table(columns=new_columns, aggfunc=lambda x: x)
        new_file = failure_file.split(".")[0] + ".json"
        json_file = df.to_json(new_file, indent=4)
        return df
    def load_failure_dictionary(json_file):
        """load json file"""
        with open(json_file, 'r') as openfile:
            # Reading from json file
            return json.load(openfile)

