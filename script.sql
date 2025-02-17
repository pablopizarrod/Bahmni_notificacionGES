create table notificacion_ges
(
    id                        int auto_increment
        primary key,
    obs_id                    int           null,
    condition_id              int           null,
    nombre_establecimiento    varchar(500)  null,
    direccion_establecimiento varchar(1000) null,
    ciudad_establecimiento    varchar(500)  null,
    notificador_id            int           null,
    nombre_notificador        varchar(500)  null,
    rut_notificador           varchar(12)   null,
    nombre_paciente           varchar(500)  null,
    rut_paciente              varchar(12)   null,
    aseguradora_paciente      varchar(300)  null,
    direccion_paciente        varchar(1000) null,
    comuna_paciente           varchar(300)  null,
    region_paciente           varchar(500)  null,
    telefono_fijo_paciente    varchar(50)   null,
    celular_paciente          varchar(50)   null,
    email_paciente            varchar(500)  not null,
    cie10                     varchar(10)   null,
    diagnostico_ges           varchar(500)  null,
    tipo                      varchar(50)   null,
    fechahora_notificacion    datetime      null,
    firma_notificador         varchar(1000) null,
    firma_paciente            text          null,
    fechahora_firma_paciente  datetime      null,
    tipo_notificado           varchar(50)   null,
    nombre_representante      varchar(500)  null,
    rut_representante         varchar(12)   null,
    telefono_representante    varchar(50)   null,
    celular_representante     varchar(50)   null,
    email_representante       varchar(500)  null,
    fechahora_registro        timestamp     null,
    fechahora_actualizacion   timestamp     null,
    usuario_registro          varchar(12)   not null,
    usuario_actualizacion     varchar(12)   null,
    estado                    char          null,
    uuid                      varchar(40)   null
);

create index notificacion_ges_rut_notificador_pk
    on notificacion_ges (rut_notificador);

create index notificacion_ges_rut_paciente_pk
    on notificacion_ges (rut_paciente);