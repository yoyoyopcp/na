import time
from flask import Flask, request, jsonify
app = Flask(__name__)

from lib import host, vol


@app.route('/2.B.latest/alerts')
def alerts():
    return jsonify({"error":[],"response":[]})

@app.route('/2.0/arrays/performance')
def perf():
    end = request.args['end_time']
    return jsonify([{u'bytes_per_mirrored_write': 0,
            u'bytes_per_op': 0,
            u'bytes_per_read': 0,
            u'bytes_per_write': 0,
            u'id': None,
            u'local_queue_usec_per_op': 0,
            u'mirrored_write_bytes_per_sec': 0,
            u'mirrored_writes_per_sec': 0,
            u'name': None,
            u'qos_rate_limit_usec_per_mirrored_write_op': 0,
            u'qos_rate_limit_usec_per_read_op': 0,
            u'qos_rate_limit_usec_per_write_op': 0,
            u'queue_depth': 0,
            u'queue_usec_per_mirrored_write_op': 0,
            u'queue_usec_per_read_op': 0,
            u'queue_usec_per_write_op': 0,
            u'read_bytes_per_sec': 0,
            u'reads_per_sec': 0,
            u'san_usec_per_mirrored_write_op': 0,
            u'san_usec_per_read_op': 0,
            u'san_usec_per_write_op': 0,
            u'service_usec_per_mirrored_write_op': 0,
            u'service_usec_per_read_op': 0,
            u'service_usec_per_write_op': 0,
            u'time': int(end)-1000*(300-i),
            u'usec_per_mirrored_write_op': 0,
            u'usec_per_read_op': 0,
            u'usec_per_write_op': 0,
            u'write_bytes_per_sec': 0,
            u'writes_per_sec': 0} for i in xrange(300)])

def total_vol_usage():
    return 75670661.0

def total_prov_size():
    return 10973347840

def raw_capacity():
    return 3766119622

@app.route('/2.0/arrays')
def arrays2():
    return jsonify({"items":[{"name":"trashy","id":"84de4d02-f435-497f-9b9c-b1a33f16b991","banner":"","console_lock_enabled":False,"idle_timeout":30,"ntp_servers":["time1.purestorage.com","time2.purestorage.com","time3.purestorage.com"],"os":"Purity//FA","scsi_timeout":60,"version":"99.9.9"}],"total_item_count":1})

@app.route('/2.B.latest/array-connections')
def array_con():
    return jsonify({"error":[],"response":[]})

@app.route('/2.B.latest/hosts')
def hosts():
    return jsonify({"error":[],"response":[{"id":44048,"apt_id":66,"view_id":128,"invalidation_id":983310,"iqn_list":["IQN.1993-08.ORG.DEBIAN:01:E3A8DF342FFB"],"nqn_list":[],"wwn_list":[],"preferred_array":[],"name":"vm-paul-carlisle","paths":{"label":"None","severity":7},"is_local":True}]})

@app.route('/2.B.latest/volumes/snapshots')
def vol_snaps():
    return jsonify({"error":[],"response":[]})

@app.route('/2.B.latest/volumes')
def vols():
    return jsonify({"error":[],"response":[{"created":1568744945176,"id":69741,"pod_id":125,"vgroup_id":31,"volume_group":"","name":"foo","serial":"84DE4D02F435497F0001106D","size":10737418240,"source_id":0,"src_apt":66,"type":"regular","host_encryption_key_status":"none"}]})

@app.route('/2.B.latest/protection_groups')
def pgroups():
    return jsonify({"error":[],"response":[]})

@app.route('/2.B.latest/volume_groups')
def vgroups():
    return jsonify({"error":[],"response":[]})


@app.route('/2.x.dev/pods')
def pods():
    return jsonify({"error":[],"response":[]})

@app.route('/2.B.latest/offload')
def offload():
    return jsonify({"error":[],"response":[]})

@app.route('/2.B.latest/service')
def service():
    return jsonify({"response":{"ready":True,"service_time":1383437689,"ready_at":1568214893392,"cold_start_time":31848,"pid":6408}})


@app.route('/2.B.latest/host_groups')
def hgroups():
    return jsonify({"error":[],"response":[]})

@app.route('/2.0/arrays/space')
def space():
    return jsonify({"items":[
        {"time":int(time.time()*1000),"name":"trashy","id":"84de4d02-f435-497f-9b9c-b1a33f16b991","space":{"data_reduction":1.0,"shared":0,"snapshots":0,"system":0,"thin_provisioning":1.0,"total_physical":total_vol_usage(),"total_provisioned":total_prov_size(),"total_reduction":1.0,"unique":total_vol_usage(),"virtual":0.0},"parity":1.0,"capacity":raw_capacity()}],"total_item_count":1})

@app.route('/2.B.latest/ports')
def ports():
    return jsonify({"error":[],"response":[
        {"name":"CT0.ETH0","target":
             {"iqn":"iqn.2010-06.com.purestorage:flasharray.71a99f64002c6db6","portal":"10.14.224.121:3260"},"failover":{}},
        {"name":"CT0.FC0","target":{"wwn":"5001500150015000","index":0},"failover":{}},
        {"name":"CT0.FC1","target":{"wwn":"5001500150015001","index":1},"failover":{}},
        {"name":"CT0.FC2","target":{"wwn":"5001500150015002","index":2},"failover":{}},
        {"name":"CT0.FC3","target":{"wwn":"5001500150015003","index":3},"failover":{}}]})


@app.route('/2.0/arrays/internal/time')
def timezone2():
    return jsonify({"error":[],"response":[{"time_zone":"America/Los_Angeles","time_offset":"-07:00","epoch_millis":1569551549897,"iso_8601":"2019-09-26T19:32:29.897-07:00"}]})

@app.route('/2.B.latest/arrays/internal/time')
def timezone():
    return jsonify({"error":[],"response":[{"time_zone":"America/Los_Angeles","time_offset":"-07:00","epoch_millis":1569551549897,"iso_8601":"2019-09-26T19:32:29.897-07:00"}]})


@app.route('/2.B.latest/drives')
def drives():
    return jsonify({"error":[],"response":[
               {"handle":"platform_SN0_Shelf0Bay_0","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY0","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_1","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY1","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_2","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY2","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_3","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY3","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_4","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY4","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_5","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY5","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_6","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY6","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_7","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY7","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_8","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY8","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_9","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY9","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_10","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY10","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_11","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY11","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_12","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY12","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_13","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY13","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"handle":"platform_SN0_Shelf0Bay_14","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY14","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":494927872},
               {"details":"Cache drive in wrong bay. Bays CH0.BAY0-CH0.BAY4294967295 supported.","handle":"platform_SN0_Shelf0Bay_15","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY15","protocol":"SAS","status":"unrecognized","raw_capacity":0},
               {"handle":"platform_SN0_Shelf0Bay_20","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY20","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":50331648},
               {"handle":"platform_SN0_Shelf0Bay_21","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY21","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":50331648},
               {"handle":"platform_SN0_Shelf0Bay_22","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY22","protocol":"SAS","status":"healthy","type":"SSD","raw_capacity":50331648},
               {"handle":"platform_SN0_Shelf0Bay_23","last_evac_completed":0,"last_failure":0,"name":"SH0.BAY23","protocol":"SAS","status":"missing","type":"SSD","raw_capacity":50331648}]
               })


@app.route('/2.B.latest/hardware')
def hardware():
    return jsonify({"error":[],"response":[
           {"handle":"FakeShelf0","index":0,"name":"SH0","parent":"hwroot", "status":"ok","type":"storage_shelf","identify_enabled":False},
           {"handle":"platform_SN0","index":0,"name":"CT0","parent":"hwroot","status":"ok","type":"controller","identify_enabled":False},
           {"handle":"platform_SN0_Shelf0Bay_20","index":20,"name":"SH0.BAY20","parent":"FakeShelf0","status":"ok","type":"drive_bay","identify_enabled":False},
           {"handle":"platform_SN0_Shelf0Bay_21","index":21,"name":"SH0.BAY21","parent":"FakeShelf0","status":"ok","type":"drive_bay","identify_enabled":False},
           {"handle":"platform_SN0_Shelf0Bay_22","index":22,"name":"SH0.BAY22","parent":"FakeShelf0","status":"ok","type":"drive_bay","identify_enabled":False},
           {"handle":"platform_SN0_Shelf0Bay_23","index":23,"name":"SH0.BAY23","parent":"FakeShelf0","status":"ok","type":"drive_bay","identify_enabled":False},
           {"handle":"platform_SN0_Shelf0PS_0","index":0,"name":"SH0.PWR0","parent":"FakeShelf0","status":"ok","type":"power_supply"},
           {"handle":"platform_SN0_Shelf0Fan_0","index":0,"name":"SH0.FAN0","parent":"FakeShelf0","status":"ok","type":"cooling"},
           {"handle":"platform_SN0_Shelf0Fan_1","index":1,"name":"SH0.FAN1","parent":"FakeShelf0","status":"ok","type":"cooling"},
           {"handle":"platform_SN0_Shelf0Fan_2","index":2,"name":"SH0.FAN2","parent":"FakeShelf0","status":"ok","type":"cooling"},
           {"handle":"platform_SN0_Shelf0Fan_3","index":3,"name":"SH0.FAN3","parent":"FakeShelf0","status":"ok","type":"cooling"},
           {"handle":"platform_SN0_Shelf0Tmp_0","index":0,"name":"SH0.TMP0","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"},
           {"handle":"platform_SN0_Shelf0Tmp_1","index":1,"name":"SH0.TMP1","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"},
           {"handle":"platform_SN0_Shelf0Tmp_2","index":2,"name":"SH0.TMP2","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"},
           {"handle":"platform_SN0_Shelf0Tmp_3","index":3,"name":"SH0.TMP3","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"},
           {"handle":"platform_SN0_Shelf0Tmp_4","index":4,"name":"SH0.TMP4","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"},
           {"handle":"platform_SN0_Shelf0Tmp_5","index":5,"name":"SH0.TMP5","parent":"FakeShelf0","status":"ok","temperature":25,"type":"temp_sensor"}]})


@app.route('/2.B.latest/maintenance-windows')
def maintenance():
    return jsonify({"error":[],"response":[]})
