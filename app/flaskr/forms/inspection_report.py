from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField, SelectField, SubmitField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import DataRequired, Optional, NumberRange


class InspectionReportForm(FlaskForm):
    task_id = SelectField(
        '作業予定',
        coerce=int,
        validators=[DataRequired(message="作業予定は必須項目です。")],
        description="作業予定を選択してください。"
    )
    
    completed_at = DateTimeLocalField(
        '実施日時', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')

    # 環境・外観等
    weather = StringField('天候', validators=[Optional()])
    temperature = FloatField('気温', validators=[Optional()])
    abnormal_odor = StringField('異常な臭気', validators=[Optional()])
    abnormal_noise_vibration = StringField('異常な騒音・振動', validators=[Optional()])

    # 検水
    water_inspection_temperature = FloatField(
        '処理水-水温', validators=[Optional()])
    water_inspection_clarity = IntegerField(
        '処理水-透視度', validators=[Optional(), NumberRange(min=0)])
    water_inspection_ph = FloatField(
        '処理水-pH', validators=[Optional(), NumberRange(min=0, max=14)])
    water_inspection_do = IntegerField(
        '処理水-DO', validators=[Optional(), NumberRange(min=0)])
    water_inspection_residual_chlorine = IntegerField(
        '処理水-残留塩素', validators=[Optional(), NumberRange(min=0)])

    # ブロワ制御機器
    blower_status_filter_cleaning = StringField(
        'ブロワ動作状況・フィルター清掃等', validators=[Optional()])

    # 躯体スラブマンホール
    manhole_damage_status = StringField(
        'マンホール等の破損状況', validators=[Optional()])
    structure_deformation_status = StringField(
        '躯体の変形・破損・浮上・沈下・水平', validators=[Optional()])
    water_leakage_status = StringField(
        '漏水の状況', validators=[Optional()])

    # 流入
    influent_foreign_matter_status = StringField(
        '流入状況（異物・油脂類の混入）', validators=[Optional()])

    # １次処理
    primary_treatment_chamber1_condition = StringField(
        '第１室の状況', validators=[Optional()])
    primary_treatment_chamber2_condition = StringField(
        '第２室の状況', validators=[Optional()])
    primary_treatment_transfer_port_condition = StringField(
        '移流口等の状況', validators=[Optional()])

    # 好気性生物反応槽（共通）
    aerobic_biological_reactor_aeration_agitation_status = StringField(
        'ばっ気撹拌の状況', validators=[Optional()])
    aerobic_biological_reactor_foaming_status = StringField(
        '発泡の状況', validators=[Optional()])

    # 接触ばっ気槽
    contact_aeration_tank_contact_material_transfer_part_status = StringField(
        '接触材・移流部の状況', validators=[Optional()])
    contact_aeration_tank_separated_sludge_status = StringField(
        '剥離汚泥の状況', validators=[Optional()])
    contact_aeration_tank_biofilm_status = StringField(
        '生物膜の状況', validators=[Optional()])
    contact_aeration_tank_backwash_device_status = StringField(
        '逆洗装置の動作状況', validators=[Optional()])

    # 担体流動槽
    carrier_fluidized_tank_carrier_condition = StringField(
        '担体の状況（磨耗等）', validators=[Optional()])
    carrier_fluidized_tank_carrier_flow_status = StringField(
        '担体の流動状況', validators=[Optional()])

    # 生物ろ過槽
    biological_filter_tank_backwash_device_condition = StringField(
        '逆洗装置の状況', validators=[Optional()])

    # 処理水槽沈殿槽
    settling_tank_overflow_weir_status = StringField(
        '越流せきの水平・固定状況', validators=[Optional()])
    settling_tank_scum_generation_status = StringField(
        'スカムの生成状況', validators=[Optional()])

    # 消毒槽
    disinfection_tank_sludge_condition = StringField(
        '汚泥の状況', validators=[Optional()])
    disinfection_tank_disinfectant_contact_status = StringField(
        '消毒剤の接触状況', validators=[Optional()])
    disinfection_tank_replenishment_amount = FloatField(
        '補充量', validators=[Optional(), NumberRange(min=0)])

    # 流入放流ポンプ槽
    pump_tank_auto_control_status = StringField(
        '自動制御機器の作動', validators=[Optional()])
    pump_tank_no1_pump_status = StringField(
        'No.1ポンプの作動状況', validators=[Optional()])
    pump_tank_no2_pump_status = StringField(
        'No.2ポンプの作動状況', validators=[Optional()])

    # 各単位装置
    unit_equipment_pest_status = StringField(
        '衛生害虫の発生状況', validators=[Optional()])
    unit_equipment_overflow_status = StringField(
        '槽内水の越流状況', validators=[Optional()])
    unit_equipment_water_level_rise_status = StringField(
        '水位上昇の状況', validators=[Optional()])
    unit_equipment_short_circuit_flow_status = StringField(
        '短絡水流の状況', validators=[Optional()])

    notes = TextAreaField('伝達事項 (管理者への伝達事項)', validators=[Optional()])

    submit = SubmitField('保存')

    def __init__(self, *args, **kwargs):
        super(InspectionReportForm, self).__init__(*args, **kwargs)
        self.task_id.choices = []
