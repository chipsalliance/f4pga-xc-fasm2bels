# Test a basic set_property with different white space formatting

# Normal
set_property PACKAGE_PIN A1 [get_ports { sig1 }]

# Indented
    set_property PACKAGE_PIN A2 [get_ports { sig2 }]

# Spaces/Tabs
set_property        PACKAGE_PIN         A3      [get_ports { sig3 }]
set_property	PACKAGE_PIN	A4	[	get_ports	{	sig4	}	]

# Dense
set_property PACKAGE_PIN A5 [get_ports {sig5}]

# Test different property names
set_property PACKAGE_PIN A6 [ get_ports { sig6 } ]
set_property PROP1 PROP_VAL [ get_ports { sig6 } ]

set_property PACKAGE_PIN A7 [ get_ports { sig7 } ]
set_property PROP_2 property123 [ get_ports { sig7 } ]

# Out of order
set_property PROP_3_3 property_abc_123 [ get_ports { sig8 } ]
set_property PACKAGE_PIN A8 [ get_ports {sig8} ]

# Test Bus Ports
set_property PACKAGE_PIN A9 [ get_ports { sig[9] } ]
set_property PACKAGE_PIN A10 [ get_ports {sig[10]} ]
set_property PACKAGE_PIN A11 [ get_ports {sig_name[11]} ]

# Change DRIVE
set_property PACKAGE_PIN A12 [ get_ports { sig12 } ]
set_property DRIVE 99 [ get_ports { sig12 } ]
