import json
import os
import sys


def get_sql_predictions_filename(predictions_filename):
    """
    Returns an output sql filename based on the given predictions filename
    """
    predictions_dir = os.path.dirname(predictions_filename)
    return os.path.join(predictions_dir, 'predictions.sql')


def format_predictions(in_filename):
    """
    Formats predicted SQL queries from a .json file to a .sql file so they can be evaluated
    """
    predicted_queries = []

    with open(in_filename, 'r') as input_file:
        all_predictions = json.loads(input_file.read())
        predicted_queries.extend(
            p['prediction'].split('| ')[-1] for p in all_predictions
        )
    out_filename = get_sql_predictions_filename(in_filename)

    with open(out_filename, 'w') as output_file:
        for q in predicted_queries:
            output_file.write(q + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("format_predictions() takes 1 argument: the predictions filename")
    else:
        predictions_file = sys.argv[1]
        format_predictions(predictions_file)
