# Test dictionary set_property

# Normal
set_property -dict { PACKAGE_PIN A1 } [get_ports { sig1 }]

# Indented
    set_property -dict { PACKAGE_PIN A2 } [get_ports { sig2 }]

# Spaces/Tabs
set_property        -dict { PACKAGE_PIN         A3    }   [get_ports { sig3 }]
set_property	-dict	{	PACKAGE_PIN	A4	}	[	get_ports	{	sig4	}	]

# Dense
set_property -dict {PACKAGE_PIN A5} [get_ports {sig5}]

# Test different property names
set_property -dict {PACKAGE_PIN A6 PROP1 PROP_VAL} [ get_ports { sig6 } ]
set_property -dict {PACKAGE_PIN A7 PROP_2 property123} [ get_ports { sig7 } ]

# Out of order
set_property -dict {PROP_3_3 property_abc_123 PACKAGE_PIN A8} [ get_ports { sig8 } ]

# Change DRIVE
set_property -dict {PACKAGE_PIN A12 DRIVE 99} [ get_ports { sig12 } ]
