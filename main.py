# Import necessary modules
from pathlib import Path
import overheads, cash_on_hand, profit_loss

# Define the main function
def main():
    # Call the overhead_function from the overheads module
    overheads.overhead_function()

    # Call the coh_function from the cash_on_hand module
    cash_on_hand.coh_function()

    # Call the profitloss_function from the profit_loss module
    profit_loss.profitloss_function()

# Call the main function to start the process
main()