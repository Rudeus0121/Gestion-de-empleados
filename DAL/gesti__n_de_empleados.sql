-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-11-2024 a las 21:28:56
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestión de empleados`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id_departamento` int(11) NOT NULL,
  `nombre_departamento` varchar(20) NOT NULL,
  `numero_departamento` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id_departamento`, `nombre_departamento`, `numero_departamento`, `habilitado_para_visualizar`) VALUES
(1, 'Recursos Humanos', 101, 0),
(2, 'Finanzas', 102, 0),
(3, 'Marketing', 103, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento_empleado`
--

CREATE TABLE `departamento_empleado` (
  `id_departamento_empleado` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_departamento` int(11) NOT NULL,
  `id_tipo_empleado` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamento_empleado`
--

INSERT INTO `departamento_empleado` (`id_departamento_empleado`, `id_empleado`, `id_departamento`, `id_tipo_empleado`, `habilitado_para_visualizar`) VALUES
(1, 1, 1, 1, 0),
(2, 2, 1, 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id_empleado` int(11) NOT NULL,
  `rut` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `direccion` varchar(40) NOT NULL,
  `telefono` int(11) NOT NULL,
  `correo_personal` varchar(35) NOT NULL,
  `fecha_inicio_contrato` date NOT NULL,
  `salario` int(11) NOT NULL,
  `id_tipo_empleado` int(11) NOT NULL,
  `id_rol_empleado` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id_empleado`, `rut`, `nombre`, `direccion`, `telefono`, `correo_personal`, `fecha_inicio_contrato`, `salario`, `id_tipo_empleado`, `id_rol_empleado`, `habilitado_para_visualizar`) VALUES
(1, 12345678, 'Juan Pérez', 'Calle Falsa 123', 5551234, 'juan@mail.com', '2024-01-01', 50000, 1, 1, 0),
(2, 87654321, 'Ana López', 'Avenida Siempreviva 742', 5555678, 'ana@mail.com', '2024-02-01', 55000, 2, 2, 0),
(4, 21963963, 'ignacio', 'pucura', 963636363, 'ignacio@gmail.com', '2024-10-01', 70000, 1, 777, 0),
(34, 21170258, 'martyn', 'hola1', 989898989, 'martyn@gmail.com', '0000-00-00', 1000, 1, 89, 0),
(777, 21931963, 'Martyn', 'jose925', 989898989, 'marty@gmail.com', '0000-00-00', 5000, 1, 777, 0),
(7777, 21612789, 'Mauricio Diaz', 'Siempre viva', 937461794, 'Mauri.dias_el_pelon@gmail.com', '2010-07-15', 1000, 1, 2, 0),
(7778, 21931963, 'Martyn', 'jose925', 989898989, 'marty@gmail.com', '0000-00-00', 5000, 1, 777, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `id_informe` int(11) NOT NULL,
  `nombre_informe` varchar(25) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `ubicacion` varchar(30) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `informe`
--

INSERT INTO `informe` (`id_informe`, `nombre_informe`, `fecha_creacion`, `ubicacion`, `id_empleado`, `habilitado_para_visualizar`) VALUES
(1, 'Informe Mensual', '2024-10-01', 'Carpeta/Informes', 1, 0),
(2, 'Informe Anual', '2024-10-30', 'Carpeta/Informes', 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `n_modulos` int(11) NOT NULL,
  `nombre_modulo` varchar(25) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `id_proyecto` int(11) NOT NULL,
  `nombre_proyecto` varchar(30) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id_proyecto`, `nombre_proyecto`, `descripcion`, `fecha_inicio`, `fecha_fin`, `habilitado_para_visualizar`) VALUES
(1, 'Proyecto A', 'Desarrollo de software', '2024-01-01', '2024-12-31', 0),
(2, 'Proyecto B', 'Investigación de mercado', '2024-02-01', '2024-11-30', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto_empleado`
--

CREATE TABLE `proyecto_empleado` (
  `id_proyecto_empleado` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `id_proyecto` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyecto_empleado`
--

INSERT INTO `proyecto_empleado` (`id_proyecto_empleado`, `id_empleado`, `id_proyecto`, `habilitado_para_visualizar`) VALUES
(1, 1, 1, 0),
(2, 2, 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `id_registro_tiempo` int(11) NOT NULL,
  `fechas` date NOT NULL,
  `horas_trabajadas` int(11) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `id_proyecto_empleado` int(11) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_tiempo`
--

INSERT INTO `registro_tiempo` (`id_registro_tiempo`, `fechas`, `horas_trabajadas`, `descripcion`, `id_proyecto_empleado`, `habilitado_para_visualizar`) VALUES
(1, '2024-10-01', 8, 'Revisión de código', 1, 0),
(2, '2024-10-02', 7, 'Documentación', 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id_rol_empleado` int(11) NOT NULL,
  `nombre_accesos` varchar(25) NOT NULL,
  `nombre_modulos` varchar(25) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado`
--

CREATE TABLE `tipo_empleado` (
  `id_tipo_empleado` int(11) NOT NULL,
  `tipo_empleado` varchar(30) NOT NULL,
  `detalle_empleado` varchar(35) NOT NULL,
  `habilitado_para_visualizar` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_empleado`
--

INSERT INTO `tipo_empleado` (`id_tipo_empleado`, `tipo_empleado`, `detalle_empleado`, `habilitado_para_visualizar`) VALUES
(1, 'Permanente', 'Empleado de planta', 0),
(2, 'Temporal', 'Empleado contratado por proyecto', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id_departamento`);

--
-- Indices de la tabla `departamento_empleado`
--
ALTER TABLE `departamento_empleado`
  ADD PRIMARY KEY (`id_departamento_empleado`),
  ADD KEY `id_empleado` (`id_empleado`,`id_departamento`,`id_tipo_empleado`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id_empleado`),
  ADD KEY `id_tipo_empleado` (`id_tipo_empleado`,`id_rol_empleado`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`id_informe`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id_proyecto`);

--
-- Indices de la tabla `proyecto_empleado`
--
ALTER TABLE `proyecto_empleado`
  ADD PRIMARY KEY (`id_proyecto_empleado`),
  ADD KEY `id_empleado` (`id_empleado`,`id_proyecto`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`id_registro_tiempo`),
  ADD KEY `id_proyecto_empleado` (`id_proyecto_empleado`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id_rol_empleado`);

--
-- Indices de la tabla `tipo_empleado`
--
ALTER TABLE `tipo_empleado`
  ADD PRIMARY KEY (`id_tipo_empleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
