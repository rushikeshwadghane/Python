from graphviz import Digraph
from datetime import datetime

# Create a Digraph object for the database architecture diagram
dot = Digraph(comment='Database Architecture for DCB and PAC Management', format='pdf')

# Global settings
dot.attr(rankdir='LR', size='10,8')

# Nodes for centralized architecture
dot.node('WebApp', 'Web Application', shape='box', style='filled', fillcolor='lightblue')
dot.node('CentralDB', 'Central Database\n(iot_control_system_db)', shape='cylinder', style='filled', fillcolor='lightgrey')
dot.edge('WebApp', 'CentralDB', label='Direct Access')

# Tables in Central DB
tables = [
    'DCBs', 'PACs', 'Sensors', 'Actuators', 'PAC Configs', 
    'DCB Configs', 'Traffic Logs', 'Users', 'Alerts'
]
for t in tables:
    dot.node(t, t, shape='note')
    dot.edge('CentralDB', t)

# Nodes for hybrid architecture
dot.node('MasterDB', 'Master DB', shape='cylinder', style='filled', fillcolor='lightyellow')
dot.node('DCB1_DB', 'DCB_001 DB', shape='cylinder', style='filled', fillcolor='lightpink')
dot.node('DCB2_DB', 'DCB_002 DB', shape='cylinder', style='filled', fillcolor='lightpink')

# Edges for hybrid setup
dot.edge('WebApp', 'MasterDB', label='Controls access')
dot.edge('MasterDB', 'DCB1_DB', label='Routes to')
dot.edge('MasterDB', 'DCB2_DB', label='Routes to')

# Label the diagram
dot.attr(label='Database Architecture Options: Centralized (Top) vs Hybrid (Bottom)', labelloc='t', fontsize='20')

# Save to PDF
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
pdf_filename = f'database_architecture_{timestamp}.pdf'
dot.render(filename=pdf_filename, cleanup=True)

print(f"PDF generated: {pdf_filename}")
