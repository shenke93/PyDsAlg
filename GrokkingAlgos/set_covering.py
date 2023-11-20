def set_covering(stations, states_needed, final_stations):
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_by_station in stations.items():
            covered = states_needed & states_by_station # covered states if the station is selected
            if len(covered) > len(states_covered): # add station or not
                best_station = station
                states_covered = covered
    
        final_stations.add(best_station) # greedy strategy: add the station cover most states
        states_needed -= states_covered # find uncovered states


if __name__ == '__main__':
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])

    final_stations = set()

    set_covering(stations, states_needed, final_stations)

    print(final_stations)