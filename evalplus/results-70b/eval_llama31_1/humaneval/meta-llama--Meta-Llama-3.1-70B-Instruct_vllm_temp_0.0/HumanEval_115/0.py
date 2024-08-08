import math

def max_fill(grid, capacity):
    """
    Calculates the minimum number of times buckets need to be lowered to empty wells in a grid.

    Args:
    grid (list): A 2D list representing the wells, where 1 indicates a unit of water.
    capacity (int): The capacity of each bucket.

    Returns:
    int: The minimum number of times buckets need to be lowered.
    """

    # Initialize the count of buckets lowered
    buckets_lowered = 0

    # Iterate over each well in the grid
    for well in grid:
        # Calculate the total water in the current well
        water_in_well = sum(well)

        # If there is water in the well, calculate how many buckets are needed
        if water_in_well > 0:
            # Calculate the number of buckets needed to empty the well
            buckets_needed = math.ceil(water_in_well / capacity)

            # Update the total count of buckets lowered
            buckets_lowered += buckets_needed

    # Return the total count of buckets lowered
    return buckets_lowered