from utils.google_sheets import *

def display_sales_report():
    sales_data = read_sales_data('Sales')
    # Code to display sales report using Streamlit
    st.title("Relatório de Vendas")
    st.dataframe(sales_data)

def insert_sales_info():
    st.title("Inserir Informações de Vendas")
    client_name = st.text_input("Nome do Cliente")
    sale_amount = st.number_input("Valor da Venda", min_value=0.0)
    sale_date = st.date_input("Data da Venda")

    if st.button("Salvar"):
        insert_sales_data(client_name, sale_amount, sale_date)
        st.success("Informações de venda inseridas com sucesso!")

def consult_sales_info():
    st.title("Consulta de Vendas")
    sale_id = st.text_input("ID da Venda")

    if st.button("Consultar"):
        sales_info = read_sales_data('Sales', sale_id)
        if sales_info:
            st.write(sales_info)
        else:
            st.error("Venda não encontrada.")

def update_sales_info():
    st.title("Alteração de Informações de Vendas")
    sale_id = st.text_input("ID da Venda")

    if st.button("Carregar Informações"):
        sales_info = read_sales_data('Sales', sale_id)
        if sales_info:
            client_name = st.text_input("Nome do Cliente", sales_info['client_name'])
            sale_amount = st.number_input("Valor da Venda", min_value=0.0, value=sales_info['sale_amount'])
            sale_date = st.date_input("Data da Venda", value=sales_info['sale_date'])

            if st.button("Atualizar"):
                update_sales_data(sale_id, client_name, sale_amount, sale_date)
                st.success("Informações de venda atualizadas com sucesso!")
        else:
            st.error("Venda não encontrada.")

def controle_vendas_screen():
    st.sidebar.title("Controle de Vendas")
    option = st.sidebar.selectbox("Escolha uma opção", ["Relatório de Vendas", "Inserir Informações", "Consultar Vendas", "Alterar Informações"])

    if option == "Relatório de Vendas":
        display_sales_report()
    elif option == "Inserir Informações":
        insert_sales_info()
    elif option == "Consultar Vendas":
        consult_sales_info()
    elif option == "Alterar Informações":
        update_sales_info()

if __name__ == "__main__":
    main()