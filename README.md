# AI Commuting Decision-Making Using Propositional Logic

## Project Overview

This project simulates AI-based decision-making for commuting options using propositional logic. The system considers multiple real-world factors—such as weather, traffic, strikes, and appointments—to suggest the best commuting method for the user: working from home, driving, or using public transport.

Additionally, for driving, the system recommends specific routes (Route A or Route B) depending on road conditions like traffic and road construction. The logic also evaluates complex decision-making based on time efficiency, convenience, and availability, providing more intelligent commuting suggestions.

## Features

- **Commuting Options**: The AI suggests whether you should work from home, drive, or take public transport based on conditions like rain, traffic, strikes, or appointments.
- **Route Selection**: If driving is recommended, the AI chooses either the regular route (Route A) or an alternative route (Route B) based on traffic and road conditions.
- **Extended Decision-Making**: Evaluates time efficiency, convenience, and availability for each option.

### Key Conditions Considered:

- **Rain**: Influences whether working from home is recommended.
- **Heavy Traffic**: Affects driving recommendations and route choices.
- **Strike**: Determines the availability of public transport.
- **Appointments**: Afternoon appointments suggest driving.
- **Road Construction**: May suggest avoiding driving or taking an alternative route.

## How to Run the Project

### Prerequisites:

- Python 3.x
- The `logic` module (provided by the course or environment)

### Steps to Run:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/FransDroid/AI-Decision-Assistant.git
   cd commuting-decisions-logic
   ```

2. **Run the Python script**:

   ```bash
   python commuting_decision.py
   ```

3. The script will simulate the decision-making process for various scenarios, such as:

   - Scenario 1: It’s raining, there’s heavy traffic, and road construction.
   - Scenario 2: There’s a public transport strike, no rain, and an afternoon appointment.
   - Scenario 3: No rain, light traffic, no strike, but road construction.

   For each scenario, the AI assistant will suggest the best commuting option and provide a breakdown of time efficiency, convenience, and availability.
