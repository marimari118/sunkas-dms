from datetime import datetime
from flaskr import db
from flaskr.models.task import Task
from flaskr.forms.inspection_report import InspectionReportForm


class InspectionReport(db.Model):
    __tablename__ = 'inspection_reports'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey(
        'tasks.id'), nullable=False, unique=True)

    completed_at = db.Column(db.DateTime, nullable=False, comment='実施日時')
    
    # 環境・外観等
    weather = db.Column(
        db.String(16), nullable=True, comment='天候')
    temperature = db.Column(
        db.Float, nullable=True, comment='気温')
    abnormal_odor = db.Column(
        db.String(16), nullable=True, comment='異常な臭気')
    abnormal_noise_vibration = db.Column(
        db.String(16), nullable=True, comment='異常な騒音・振動')

    # 検水
    water_inspection_temperature = db.Column(
        db.Float, nullable=True, comment='検水 処理水-水温')
    water_inspection_clarity = db.Column(
        db.Integer, nullable=True, comment='検水 処理水-透視度')
    water_inspection_ph = db.Column(
        db.Float, nullable=True, comment='検水 処理水-pH')
    water_inspection_do = db.Column(
        db.Integer, nullable=True, comment='検水 処理水-DO')
    water_inspection_residual_chlorine = db.Column(
        db.Integer, nullable=True, comment='検水 処理水-残留塩素')

    # ブロワ制御機器
    blower_status_filter_cleaning = db.Column(
        db.Text, nullable=True, comment='ブロワ制御機器-ブロワ動作状況・フィルター清掃等')

    # 躯体スラブマンホール
    manhole_damage_status = db.Column(
        db.String(16), nullable=True, comment='躯体スラブマンホール-マンホール等の破損状況')
    structure_deformation_status = db.Column(
        db.String(16), nullable=True, comment='躯体スラブマンホール-躯体の変形・破損・浮上・沈下・水平')
    water_leakage_status = db.Column(
        db.String(16), nullable=True, comment='躯体スラブマンホール-漏水の状況')

    # 流入
    influent_foreign_matter_status = db.Column(
        db.String(16), nullable=True, comment='流入-流入状況（異物・油脂類の混入）')

    # １次処理
    primary_treatment_chamber1_condition = db.Column(
        db.String(16), nullable=True, comment='１次処理-第１室の状況')
    primary_treatment_chamber2_condition = db.Column(
        db.String(16), nullable=True, comment='１次処理-第２室の状況')
    primary_treatment_transfer_port_condition = db.Column(
        db.String(16), nullable=True, comment='１次処理-移流口等の状況')

    # 好気性生物反応槽（共通）
    aerobic_biological_reactor_aeration_agitation_status = db.Column(
        db.String(16), nullable=True, comment='好気性生物反応槽（共通）-ばっ気撹拌の状況')
    aerobic_biological_reactor_foaming_status = db.Column(
        db.String(16), nullable=True, comment='好気性生物反応槽（共通）-発泡の状況')

    # 接触ばっ気槽
    contact_aeration_tank_contact_material_transfer_part_status = db.Column(
        db.String(16), nullable=True, comment='接触ばっ気槽-接触材・移流部の状況')
    contact_aeration_tank_separated_sludge_status = db.Column(
        db.String(16), nullable=True, comment='接触ばっ気槽-剥離汚泥の状況')
    contact_aeration_tank_biofilm_status = db.Column(
        db.String(16), nullable=True, comment='接触ばっ気槽-生物膜の状況')
    contact_aeration_tank_backwash_device_status = db.Column(
        db.String(16), nullable=True, comment='接触ばっ気槽-逆洗装置の動作状況')

    # 担体流動槽
    carrier_fluidized_tank_carrier_condition = db.Column(
        db.String(16), nullable=True, comment='担体流動槽-担体の状況（磨耗等）')
    carrier_fluidized_tank_carrier_flow_status = db.Column(
        db.String(16), nullable=True, comment='担体流動槽-担体の流動状況')

    # 生物ろ過槽
    biological_filter_tank_backwash_device_condition = db.Column(
        db.String(16), nullable=True, comment='生物ろ過槽-逆洗装置の状況')

    # 処理水槽沈殿槽
    settling_tank_overflow_weir_status = db.Column(
        db.String(16), nullable=True, comment='処理水槽沈殿槽-越流せきの水平・固定状況')
    settling_tank_scum_generation_status = db.Column(
        db.String(16), nullable=True, comment='処理水槽沈殿槽-スカムの生成状況')

    # 消毒槽
    disinfection_tank_sludge_condition = db.Column(
        db.String(16), nullable=True, comment='消毒槽-汚泥の状況')
    disinfection_tank_disinfectant_contact_status = db.Column(
        db.String(16), nullable=True, comment='消毒槽-消毒剤の接触状況')
    disinfection_tank_replenishment_amount = db.Column(
        db.Float, nullable=True, comment='消毒槽-補充量')

    # 流入放流ポンプ槽
    pump_tank_auto_control_status = db.Column(
        db.String(16), nullable=True, comment='流入放流ポンプ槽-自動制御機器の作動')
    pump_tank_no1_pump_status = db.Column(
        db.String(16), nullable=True, comment='流入放流ポンプ槽-No.1ポンプの作動状況')
    pump_tank_no2_pump_status = db.Column(
        db.String(255), nullable=True, comment='流入放流ポンプ槽-No.2ポンプの作動状況')

    # 各単位装置
    unit_equipment_pest_status = db.Column(
        db.String(16), nullable=True, comment='各単位装置-衛生害虫の発生状況')
    unit_equipment_overflow_status = db.Column(
        db.String(16), nullable=True, comment='各単位装置-槽内水の越流状況')
    unit_equipment_water_level_rise_status = db.Column(
        db.String(16), nullable=True, comment='各単位装置-水位上昇の状況')
    unit_equipment_short_circuit_flow_status = db.Column(
        db.String(16), nullable=True, comment='各単位装置-短絡水流の状況')
    
    notes = db.Column(db.Text, nullable=True, comment='伝達事項 (管理者への伝達事項)')

    created_at = db.Column(db.DateTime,
        default=datetime.now,
        nullable=False)
    updated_at = db.Column(db.DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False)

    task = db.relationship(Task,
        backref=db.backref('inspection_report', uselist=False, cascade="all, delete-orphan"))
    
    @staticmethod
    def form(form: InspectionReportForm):
        return InspectionReport(
            task_id = form.task_id.data,
            completed_at = form.completed_at.data,
            weather = form.weather.data,
            temperature = form.temperature.data,
            abnormal_odor = form.abnormal_odor.data,
            abnormal_noise_vibration = form.abnormal_noise_vibration.data,
            water_inspection_temperature = form.water_inspection_temperature.data,
            water_inspection_clarity = form.water_inspection_clarity.data,
            water_inspection_ph = form.water_inspection_ph.data,
            water_inspection_do = form.water_inspection_do.data,
            water_inspection_residual_chlorine = form.water_inspection_residual_chlorine.data,
            blower_status_filter_cleaning = form.blower_status_filter_cleaning.data,
            manhole_damage_status = form.manhole_damage_status.data,
            structure_deformation_status = form.structure_deformation_status.data,
            water_leakage_status = form.water_leakage_status.data,
            influent_foreign_matter_status = form.influent_foreign_matter_status.data,
            primary_treatment_chamber1_condition = form.primary_treatment_chamber1_condition.data,
            primary_treatment_chamber2_condition = form.primary_treatment_chamber2_condition.data,
            primary_treatment_transfer_port_condition = form.primary_treatment_transfer_port_condition.data,
            aerobic_biological_reactor_aeration_agitation_status = form.aerobic_biological_reactor_aeration_agitation_status.data,
            aerobic_biological_reactor_foaming_status = form.aerobic_biological_reactor_foaming_status.data,
            contact_aeration_tank_contact_material_transfer_part_status = form.contact_aeration_tank_contact_material_transfer_part_status.data,
            contact_aeration_tank_separated_sludge_status = form.contact_aeration_tank_separated_sludge_status.data,
            contact_aeration_tank_biofilm_status = form.contact_aeration_tank_biofilm_status.data,
            contact_aeration_tank_backwash_device_status = form.contact_aeration_tank_backwash_device_status.data,
            carrier_fluidized_tank_carrier_condition = form.carrier_fluidized_tank_carrier_condition.data,
            carrier_fluidized_tank_carrier_flow_status = form.carrier_fluidized_tank_carrier_flow_status.data,
            biological_filter_tank_backwash_device_condition = form.biological_filter_tank_backwash_device_condition.data,
            settling_tank_overflow_weir_status = form.settling_tank_overflow_weir_status.data,
            settling_tank_scum_generation_status = form.settling_tank_scum_generation_status.data,
            disinfection_tank_sludge_condition = form.disinfection_tank_sludge_condition.data,
            disinfection_tank_disinfectant_contact_status = form.disinfection_tank_disinfectant_contact_status.data,
            disinfection_tank_replenishment_amount = form.disinfection_tank_replenishment_amount.data,
            pump_tank_auto_control_status = form.pump_tank_auto_control_status.data,
            pump_tank_no1_pump_status = form.pump_tank_no1_pump_status.data,
            pump_tank_no2_pump_status = form.pump_tank_no2_pump_status.data,
            unit_equipment_pest_status = form.unit_equipment_pest_status.data,
            unit_equipment_overflow_status = form.unit_equipment_overflow_status.data,
            unit_equipment_water_level_rise_status = form.unit_equipment_water_level_rise_status.data,
            unit_equipment_short_circuit_flow_status = form.unit_equipment_short_circuit_flow_status.data,
            notes = form.notes.data)
        
    def apply(self, form: InspectionReportForm):
        self.task_id = form.task_id.data
        self.completed_at = form.completed_at.data
        self.weather = form.weather.data
        self.temperature = form.temperature.data
        self.abnormal_odor = form.abnormal_odor.data
        self.abnormal_noise_vibration = form.abnormal_noise_vibration.data
        self.water_inspection_temperature = form.water_inspection_temperature.data
        self.water_inspection_clarity = form.water_inspection_clarity.data
        self.water_inspection_ph = form.water_inspection_ph.data
        self.water_inspection_do = form.water_inspection_do.data
        self.water_inspection_residual_chlorine = form.water_inspection_residual_chlorine.data
        self.blower_status_filter_cleaning = form.blower_status_filter_cleaning.data
        self.manhole_damage_status = form.manhole_damage_status.data
        self.structure_deformation_status = form.structure_deformation_status.data
        self.water_leakage_status = form.water_leakage_status.data
        self.influent_foreign_matter_status = form.influent_foreign_matter_status.data
        self.primary_treatment_chamber1_condition = form.primary_treatment_chamber1_condition.data
        self.primary_treatment_chamber2_condition = form.primary_treatment_chamber2_condition.data
        self.primary_treatment_transfer_port_condition = form.primary_treatment_transfer_port_condition.data
        self.aerobic_biological_reactor_aeration_agitation_status = form.aerobic_biological_reactor_aeration_agitation_status.data
        self.aerobic_biological_reactor_foaming_status = form.aerobic_biological_reactor_foaming_status.data
        self.contact_aeration_tank_contact_material_transfer_part_status = form.contact_aeration_tank_contact_material_transfer_part_status.data
        self.contact_aeration_tank_separated_sludge_status = form.contact_aeration_tank_separated_sludge_status.data
        self.contact_aeration_tank_biofilm_status = form.contact_aeration_tank_biofilm_status.data
        self.contact_aeration_tank_backwash_device_status = form.contact_aeration_tank_backwash_device_status.data
        self.carrier_fluidized_tank_carrier_condition = form.carrier_fluidized_tank_carrier_condition.data
        self.carrier_fluidized_tank_carrier_flow_status = form.carrier_fluidized_tank_carrier_flow_status.data
        self.biological_filter_tank_backwash_device_condition = form.biological_filter_tank_backwash_device_condition.data
        self.settling_tank_overflow_weir_status = form.settling_tank_overflow_weir_status.data
        self.settling_tank_scum_generation_status = form.settling_tank_scum_generation_status.data
        self.disinfection_tank_sludge_condition = form.disinfection_tank_sludge_condition.data
        self.disinfection_tank_disinfectant_contact_status = form.disinfection_tank_disinfectant_contact_status.data
        self.disinfection_tank_replenishment_amount = form.disinfection_tank_replenishment_amount.data
        self.pump_tank_auto_control_status = form.pump_tank_auto_control_status.data
        self.pump_tank_no1_pump_status = form.pump_tank_no1_pump_status.data
        self.pump_tank_no2_pump_status = form.pump_tank_no2_pump_status.data
        self.unit_equipment_pest_status = form.unit_equipment_pest_status.data
        self.unit_equipment_overflow_status = form.unit_equipment_overflow_status.data
        self.unit_equipment_water_level_rise_status = form.unit_equipment_water_level_rise_status.data
        self.unit_equipment_short_circuit_flow_status = form.unit_equipment_short_circuit_flow_status.data
        self.notes = form.notes.data

    def __repr__(self):
        return f'<InspectionReport {self.id} for Task {self.task_id}>'
