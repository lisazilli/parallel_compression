set pkgmbrs=
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cpc\Cpc.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cmi\Cmi.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cui\Web\CuiWeb.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfc\Visa\CfcVisa.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfc\Mcrd\CfcMcrd.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Mony\CfeMony.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Cnx\CfeCnxV1.3.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Vnet\CfeVnet.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Shzm\CfeShzm.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\B24es\CfeB24ES.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Dsdb\CfeDsdb.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Nyce\CfeNyce.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Edse\CfeEdse.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Link\CfeLink.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Mds\CfeMds.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Upi\CfeUpi.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Mipm\CfeMipm.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\B24v60\CfeB24V6.0.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Fepc\CfeFepc.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Vsms\CfeVsms.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Affn\CfeAffn.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Stw\CfeStw.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Stne\CfeStne.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Mps\CfeMps.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Bhm\CfeBhm.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Efnd\CfeEfnd.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Athcv34\CfeAthcV3.4.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Cup\CfeCup.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cfe\Dcas\CfeDcas.4.3.13_Stable_Oracle
set pkgmbrs=%pkgmbrs% L:\Prj\CpsPkgCapstone\Cce\Bhm\Cce.4.3.13_Stable_Oracle

rem
rem    Ask user for the total number of processors to perform compression
rem
set /p nbrprcr="How many processors would you like to use to perform compression? "

@echo Started: %date% %time%
if exist L:\Prj\CpsPkgCapstone\Compressed del /q L:\Prj\CpsPkgCapstone\Compressed
python Compress.py %pkgmbrs% L:\Prj\CpsPkgCapstone\Compressed %nbrprcr%
@echo Ended: %date% %time%
