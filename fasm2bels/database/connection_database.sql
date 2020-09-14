-- This is the database schema for relating a tile grid to a VPR routing
-- graph.
--
-- Terms:
--  grid - A 2D matrix of tiles
--
--  phy_tile - A location with the physical grid.  A tile is always of a
--         particular tile type.  The tile type specifies what wires, pips and
--         sites a tile contains.
--
--         The physical grid is defined by the underlying hardware, and has
--         expliotable regularity.  However it is not ideal to place using this
--         grid, as there are various empty tiles to match the hardware (e.g.
--         VBRK tiles).
--
--  tile - A location within the VPR grid.  A tile is always of a partial
--         tile type.  The tile type specifies what wires, pips and
--         sites a tile contains.
--
--         The VRP grid may have one phy_tile split across two tiles (e.g.
--         CLBLL_L) or may combine multiple phy_tile's into one (e.g. INT_L
--         into the tile to it's left.
--
--         This table contains the information on the grid output to arch.xml.
--
--  wires - A partial net within a tile.  It may start or end at a site pins
--          or a pip, or can connect to wires in other tiles.
--
--  pip - Programable interconnect point, connecting two wires within a
--        tile.
--
--  node - A complete net made of one or more wires.
--
--  site - A location within a tile that contains site pins and BELs.
--         BELs are not described in this database.
--
--  site - Site pins are the connections to/from the site to a wire in a
--         tile.  A site pin may be associated with one wire in the tile.
--
--  graph_node - A VPR type representing either a pb_type IPIN or OPIN or
--               a routing wire CHANX or CHANY.
--
--               IPIN/OPIN are similiar to site pin.
--               CHANX/CHANY are how VPR express routing nodes.
--
--  track - A collection of graph_node's that represents one routing node.
--
--  graph_edge - A VPR type representing a connection between an IPIN, OPIN,
--               CHANX, or CHANY.  All graph_edge's require a switch.
--
--  switch - See VPR documentation :http://docs.verilogtorouting.org/en/latest/arch/reference/--tag-fpga-device-information-switch_block
--
--  This database provides a relational description between the terms above.

-- Tile type table, used to track tile_type using a pkey, and provide
-- the tile_type_pkey <-> name mapping.
CREATE TABLE tile_type(
  pkey INTEGER PRIMARY KEY,
  name TEXT
);

-- Site type table, used to track site_type using a pkey, and provide
-- the site_type_pkey <-> name mapping.
CREATE TABLE site_type(
  pkey INTEGER PRIMARY KEY,
  name TEXT
);

-- Physical tile table, contains type and name of tile and location in the prjxray grid.
CREATE TABLE phy_tile(
  pkey INTEGER PRIMARY KEY,
  name TEXT,
  tile_type_pkey INT,
  grid_x INT,
  grid_y INT,
  clock_region_pkey INT,
  FOREIGN KEY(tile_type_pkey) REFERENCES tile_type(pkey),
  FOREIGN KEY(clock_region_pkey) REFERENCES clock_region(pkey)
);

-- Site pin table, contains names of pins and their direction, along
-- with parent site type information.
CREATE TABLE site_pin(
  pkey INTEGER PRIMARY KEY,
  name TEXT,
  site_type_pkey INT,
  direction TEXT,
  FOREIGN KEY(site_type_pkey) REFERENCES site_type(pkey)
);

-- Concreate site instance within tiles.  Used to relate connect
-- wire_in_tile instead to site_type's, along with providing metadata
-- about the site.
CREATE TABLE site(
  pkey INTEGER PRIMARY KEY,
  name TEXT,
  x_coord INT,
  y_coord INT,
  site_type_pkey INT,
  tile_type_pkey INT,
  FOREIGN KEY(site_type_pkey) REFERENCES site_type(pkey),
  FOREIGN KEY(tile_type_pkey) REFERENCES tile_type(pkey)
);

-- Table recording each site instance in the grid, useful for lookups.
CREATE TABLE site_instance(
    pkey INTEGER PRIMARY KEY,
    name TEXT,
    x_coord INT,
    y_coord INT,
    site_pkey INT,
    phy_tile_pkey INT,
    prohibited BOOLEAN,
    FOREIGN KEY(site_pkey) REFERENCES site(pkey),
    FOREIGN KEY(phy_tile_pkey) REFERENCES phy_tile(pkey)
);

-- Table of tile type wires. This table is the of uninstanced tile type
-- wires. Site pins wires will reference their site and site pin rows in
-- the site and site_pin tables.
--
-- All concrete wire instances will related to a row in this table.
CREATE TABLE wire_in_tile(
  pkey INTEGER PRIMARY KEY,
  name TEXT,
  phy_tile_type_pkey INT,
  tile_type_pkey INT,
  site_pkey INT,
  site_pin_pkey INT,
  FOREIGN KEY(phy_tile_type_pkey) REFERENCES phy_tile_type(pkey),
  FOREIGN KEY(tile_type_pkey) REFERENCES tile_type(pkey),
  FOREIGN KEY(site_pkey) REFERENCES site(pkey),
  FOREIGN KEY(site_pin_pkey) REFERENCES site_pin(pkey)
);

-- Table of nodes.  Provides the concrete relation for connected wire
-- instances. Generally speaking nodes are either routing nodes or a site
-- pin node.
--
-- Routing nodes will have track_pkey set.
-- Site pin nodes will have a site_wire_pkey to the wire that is the wire
-- connected to a site pin.
CREATE TABLE node(
  pkey INTEGER PRIMARY KEY,
  number_pips INT,
  track_pkey INT,
  site_wire_pkey INT,
  classification INT,
  FOREIGN KEY(track_pkey) REFERENCES track_pkey(pkey),
  FOREIGN KEY(site_wire_pkey) REFERENCES wire(pkey)
);

-- Table of wires.  This table is the complete list of all wires in the
-- grid. All wires will belong to exactly one node.
--
-- Rows will relate back to their parent tile, and generic wire instance.
--
-- If the wire is connected to both a site pin and a pip, then
-- top_graph_node_pkey, bottom_graph_node_pkey, left_graph_node_pkey, and
-- right_graph_node_pkey will be set to the IPIN or OPIN instances, based
-- on the pin directions for the tile.
--
-- If the wire is a member of a routing node, then graph_node_pkey will be
-- set to the graph_node this wire is a member of.
--
-- The wire has two columns for tile location.  phy_tile_pkey points to the
-- physical prjxray tile that contains this wire.  The tile_pkey points to the
-- VPR tile that contains this wire.
--
-- Do note that unless this wire is connected to a IPIN or OPIN, VPR does not
-- model exact tile locations for wires.  Instead the wire will have been
-- lumped into a CHANX or CHANY node.
CREATE TABLE wire(
  pkey INTEGER PRIMARY KEY,
  node_pkey INT,
  phy_tile_pkey INT,
  tile_pkey INT,
  wire_in_tile_pkey INT,
  graph_node_pkey INT,
  top_graph_node_pkey INT,
  bottom_graph_node_pkey INT,
  left_graph_node_pkey INT,
  right_graph_node_pkey INT,
  site_pin_graph_node_pkey INT,
  FOREIGN KEY(node_pkey) REFERENCES node(pkey),
  FOREIGN KEY(phy_tile_pkey) REFERENCES phy_tile(pkey),
  FOREIGN KEY(tile_pkey) REFERENCES tile(pkey),
  FOREIGN KEY(wire_in_tile_pkey) REFERENCES wire_in_tile(pkey),
  FOREIGN KEY(graph_node_pkey) REFERENCES graph_node(pkey),
  FOREIGN KEY(top_graph_node_pkey) REFERENCES graph_node(pkey),
  FOREIGN KEY(bottom_graph_node_pkey) REFERENCES graph_node(pkey),
  FOREIGN KEY(left_graph_node_pkey) REFERENCES graph_node(pkey),
  FOREIGN KEY(right_graph_node_pkey) REFERENCES graph_node(pkey),
  FOREIGN KEY(site_pin_graph_node_pkey) REFERENCES graph_node(pkey)
);
