# Ticket Agency App

## Overview
The Ticket Agency App is a Streamlit-based application designed for managing ticket sales, client information, and financial projections for a ticket agency. The application connects to Google Sheets to read and write data, providing a user-friendly interface for various functionalities.

## Project Structure
```
ticket-agency-app
├── src
│   ├── app.py                  # Main entry point of the Streamlit application
│   ├── crm_clientes.py         # CRM Clientes functionalities
│   ├── milheiros.py             # Milheiros functionalities
│   ├── agencias.py              # Agências functionalities
│   ├── controle_compras.py      # Controle de Compras functionalities
│   ├── controle_vendas.py       # Controle de Vendas functionalities
│   ├── controle_emissoes.py     # Controle de Emissões de Voos functionalities
│   ├── fluxo_caixa.py          # Controle do Fluxo de Caixa report
│   ├── match_margens.py        # Match de Margens report
│   ├── projecao_financeira.py  # Projeção Financeira functionalities
│   ├── calculadoras.py          # Calculadoras functionalities
│   └── utils
│       └── google_sheets.py    # Utility functions for Google Sheets integration
├── requirements.txt             # List of dependencies
└── README.md                    # Project documentation
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ticket-agency-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
streamlit run src/app.py
```

## Features
- **CRM Clientes**: Manage client information with options to insert, consult, and alter data.
- **Milheiros**: Handle milheiro information with functionalities for insertion, consultation, and alteration.
- **Agências**: Manage agency data with options to insert, consult, and alter information.
- **Controle de Compras**: Generate purchase reports and manage purchase information.
- **Controle de Vendas**: Generate sales reports and manage sales information.
- **Controle de Emissões de Voos**: Monitor the status of flight emissions and manage related data.
- **Controle do Fluxo de Caixa**: View a report of cash flow without tabs.
- **Match de Margens**: View a report on margin matching without tabs.
- **Projeção Financeira**: Manage financial projections.
- **Calculadoras**: Tools for converting miles and calculating margins for flights paid in foreign currencies.

## Google Sheets Integration
The application utilizes Google Sheets for data storage and retrieval. Ensure you have the necessary credentials and permissions set up to access the Google Sheets API.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.