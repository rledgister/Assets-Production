module go_somewhere_significant {
  import unit;
  import universe;
  object destination;
  object significantun;
  bool baseonly;
  bool capship;
  bool jumppoint;
  bool arrivedsys;
  bool arrivedarea;
  float distfrombase;
  object youcontainer;
  bool HaveArrived () {
    return arrivedarea;
  };
  bool InSystem() {
    return arrivedsys;
  };
  //only run this function if we are InSystem();
  object SignificantUnit() {
    if (_std.isNull(significantun)) {
      return significantun;
    }
    return _unit.getUnitFromContainer (significantun);
  };
  object DestinationSystem () {
    return destination;
  };
  void init_base_only (object you, int numsystemsaway, float distance_away_to_trigger) {
    init (you,numsystemsaway,true,false,distance_away_to_trigger);
    baseonly = true;
  };
  void init (object you, int numsystemsaway, bool capship_only, bool jumppoint_only,  float distance_away_to_trigger) {
    _std.setNull ( significantun);
    youcontainer = _unit.getContainer (you);
    capship = capship_only;
    jumppoint = jumppoint_only;
    baseonly=false;
    distfrombase=distance_away_to_trigger;
    object sysfile = _std.getSystemFile();
    destination=universe.getAdjacentSystem(sysfile,numsystemsaway);
    arrivedsys=false;
    arrivedarea=false;
  };
  void destroy() {
    _unit.deleteContainer (youcontainer);
    _std.setNull(youcontainer);
    _string.delete (destination);
    _std.setNull(destination);
    if (arrivedsys) {
      if (!_std.isNull(significantun)) {
	_unit.deleteContainer (significantun);
	_std.setNull(significantun);
      }
    }
  };
  void loop() {
	  if (arrivedsys) {
	    object base=_unit.getUnitFromContainer(significantun);
	    object you=_unit.getUnitFromContainer(youcontainer);
	    if (_std.isNull(base)||_std.isNull(you)) {
	      return;
	    }
	    float dist=_unit.getDistance(base,you);
	    if (dist<=distfrombase) {
	      arrivedarea=true;
	    }
	  } else if (!arrivedsys) {
	    object sysfil = _std.getSystemFile();
	    if (_string.equal (sysfil,destination)) {
	      arrivedsys=true;
	      object significant;
	      if (capship) {
		int randint=random.randomint(0,128);
		significant = unit.getSignificant (randint,capship,baseonly);
	      }else {
		significant = universe.getRandomJumppoint ();
	      }
	      if (_std.isNull (significant)) {
		significant =_unit.getPlayer();
	      }
	      if (_std.isNull(significant)) {
		arrivedsys=false;
	      }else {
		object newun=significant;
		object str = _string.new();
		object name = _unit.getName (newun);
		_io.sprintf(str,"You must visit the %s",name);
		_string.delete (name);
		_io.message (0,"game","all",str);
		_string.delete(str);
       		significantun=_unit.getContainer(significant);
	      }
	    }
	    _string.delete (sysfil);
	  }    

  };
}
