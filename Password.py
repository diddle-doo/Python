# Tableau 
# This is a program that changes the password of all workbooks that has published datasource


import tableauserverclient as TSC
from tableauserverclient.server.endpoint import workbooks_endpoint
from tableauserverclient.models import connection_item

tableau_auth = TSC.TableauAuth('username', 'password')
server = TSC.Server('https://tableau.com/')
server.auth.sign_in(tableau_auth)
print('Starting the update work ..')
print('Server site id is ', server.site_id)
print('Server base url is ', server.baseurl)
print('Server namespace is ', server.namespace)
_site_id = server.site_id
master_password = 'dummypassword'  # change this to master password #masterpassword
no_of_updates = 0


def update_connections(workbook, site_id, conn_id, is_embed=True):
    print('Connection for ', workbook.name, ' is going to get updated')
    connect_item = connection_item.ConnectionItem()
    connect_item._id = conn_id
    connect_item.password = master_password
    connect_item.embed_password = is_embed
    # if you have to change the username also, uncomment this
    # connect_item.username = '<your_username>'
    work_book = workbooks_endpoint.Workbooks(server)
    connect_item = work_book.update_connection(workbook, connect_item)
    print('Connection details are updated successfully of workbook ', workbook.name)


for wb in TSC.Pager(server.workbooks):
    wb_id = wb.id  # the workbook id and from this we can update the connection details
    project_id = wb.project_id
    connection = server.workbooks.populate_connections(wb)
    '''
    URL to update :  http://tableau.com/api/2.3/sites/_site_id/workbooks/wb_id/connections/connection_id
            Data : 
            <tsRequest>
              <connection
                password="masterpassword" 
                embedPassword="True"  />
            </tsRequest>
    '''
    for wb_item in wb.connections:
        if wb_item.connection_type == 'sqlserver' and wb_item.username == 'username' and wb_item.datasource_name == 'dummy-workbook':
            print('------------------------------------*********************------------------------------------------')
            print('project details are project name ', wb.project_name, ' and project id is ', project_id,
                  ' and workbook name is ', wb.name, ' and workbook id is ', wb_id)
            connection_id = wb_item.id
            update_connections(wb, _site_id, connection_id, is_embed=True)  # set is_embed True or False for workbook
            no_of_updates += 1
            print('------------------------------------*********************------------------------------------------')
            print('Total workbooks updated : ', no_of_updates)
# the end process
server.auth.sign_out()
