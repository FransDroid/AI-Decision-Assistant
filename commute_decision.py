from logic import *

# Define the conditions as symbols
Rain = Symbol("rain")
HeavyTraffic = Symbol("heavyTraffic")
EarlyMeeting = Symbol("earlyMeeting")
Strike = Symbol("strike")
Appointment = Symbol("appointment")
Afternoon = Symbol("afternoon")
RoadConstruction = Symbol("roadConstruction")

# Define commuting options as symbols
WFH = Symbol("workFromHome")  
Drive = Symbol("drive")       
PublicTransport = Symbol("publicTransport")  

# Define routes as symbols for driving
RouteA = Symbol("routeA")  # Regular route
RouteB = Symbol("routeB")  # Alternative route (to avoid road construction or heavy traffic)


# Define factors for complex decision-making (for bonus task)
Convenient = Symbol("convenient")
Available = Symbol("available")
TimeEfficient = Symbol("timeEfficient")

# Create the knowledge base
knowledge = And(
    Implication(Or(Rain, EarlyMeeting), WFH),  # If it's raining or there’s an early meeting, you should work from home.
    Implication(And(Not(Rain), Not(HeavyTraffic)), Drive), # If it’s not raining and there’s no heavy traffic, you should drive.
    Implication(And(Not(Strike), Not(Rain)), PublicTransport), # If there’s no strike and it’s not raining, you should take public transport.

    # Additional transport rules
    Implication(And(Appointment, Afternoon), Drive),  # If you have a doctor's appointment in the afternoon, drive.
    Implication(RoadConstruction, Not(Drive)),  # If there's road construction, avoid driving.
    
    # Route selection when driving
    Implication(And(Drive, Not(RoadConstruction), Not(HeavyTraffic)), RouteA),  # Use Route A (regular) if no road construction or heavy traffic.
    Implication(And(Drive, Or(RoadConstruction, HeavyTraffic)), RouteB),  # Use Route B (alternative) if there's road construction or heavy traffic.
    
    # Extended rules for time, cost, and convenience
    Implication(And(Drive, RoadConstruction), Not(Convenient)),  # Driving is not convenient with road construction.
    Implication(And(PublicTransport, Strike), Not(Available)),  # Public transport is not available during a strike.
    Implication(And(WFH, Or(Rain, EarlyMeeting)), TimeEfficient),  # Working from home is time-efficient during bad weather or early meetings.
)

# Queries
query_wfh = WFH # Query 1: Should you work from home
query_drive = Drive # Query 2: Should you drive (Drive)?
query_public_transport = PublicTransport # Query 3: Should you take public transport (PublicTransport)?


# Function to perform model checking for the most suitable option
def check_option(scenario):
    combined_knowledge = And(knowledge, And(*scenario))
    
    # Determine best commuting option first
    if model_check(combined_knowledge, WFH):
        return "Work From Home"
    elif model_check(combined_knowledge, Drive):
        # Check which route to take if driving
        if model_check(combined_knowledge, RouteA):
            return "Drive (Route A - Regular)"
        elif model_check(combined_knowledge, RouteB):
            return "Drive (Route B - Alternative)"
    elif model_check(combined_knowledge, PublicTransport):
        return "Public Transport"
    else:
        return "No suitable option found"

# Function to evaluate complex decision-making (based on time, cost, and convenience)
def check_complex_decision(scenario):
    combined_knowledge = And(knowledge, And(*scenario))
    
    # Analyze based on time, cost, and convenience
    return {
        "Time Efficient": model_check(combined_knowledge, TimeEfficient),
        "Convenient": model_check(combined_knowledge, Convenient),
        "Available": model_check(combined_knowledge, Available)
    }

# Updated scenarios with new conditions
scenario_1 = {Rain, HeavyTraffic, RoadConstruction}  # It's raining, heavy traffic, and road construction.
scenario_2 = {Strike, Not(Rain), Appointment, Afternoon}  # Public transport strike, no rain, afternoon appointment.
scenario_3 = {Not(Rain), Not(HeavyTraffic), Not(Strike), RoadConstruction}  # No rain, light traffic, no strike, road construction.

# Check scenarios
scenarios = [
    ("Scenario 1 (It’s raining, heavy traffic, and road construction.)", scenario_1),
    ("Scenario 2 (Public transport strike, no rain, and afternoon appointment)", scenario_2),
    ("Scenario 3 (No rain, light traffic, no strike, but road construction.)", scenario_3)
]

for scenario_name, scenario in scenarios:
    print(f"\n{scenario_name}:")
    result = check_option(scenario)
    print(f"  Suggested option: {result}")

    # Check for more complex decision-making (time, cost, convenience)
    decision_analysis = check_complex_decision(scenario)
    print(f"  Time Efficient: {decision_analysis['Time Efficient']}")
    print(f"  Convenient: {decision_analysis['Convenient']}")
    print(f"  Available: {decision_analysis['Available']}")